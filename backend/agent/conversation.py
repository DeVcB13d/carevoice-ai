"""Agent conversation loop and state management."""

import uuid
import json
from typing import Optional
from dataclasses import dataclass
from datetime import datetime

from livekit.agents import Agent, function_tool
from livekit.agents.inference import STT, TTS, LLM

from backend.config import Config
from backend.agent.prompts import SYSTEM_PROMPT
from backend.db import get_db


@dataclass
class ConversationState:
    """State maintained during a conversation."""

    call_id: str
    user_id: Optional[int] = None
    user_name: Optional[str] = None
    user_phone: Optional[str] = None
    extracted_date: Optional[str] = None
    extracted_time: Optional[str] = None
    booked_slot_id: Optional[int] = None
    message_count: int = 0
    started_at: datetime = None

    def __post_init__(self):
        if self.started_at is None:
            self.started_at = datetime.now()


class HealthcareAgent(Agent):
    """Healthcare appointment booking agent."""

    def __init__(
        self,
        user_id: Optional[int] = None,
        user_name: Optional[str] = None,
        user_phone: Optional[str] = None,
        instructions: str = SYSTEM_PROMPT,
    ):
        """Initialize the agent with APIs."""
        Config.validate()

        self.state = ConversationState(
            call_id=str(uuid.uuid4()),
            user_id=user_id,
            user_name=user_name,
            user_phone=user_phone,
        )
        self.room = None
        self.conversation_history = []

        # Initialize STT (Speech-to-Text) using LiveKit Inference
        stt = STT(model="deepgram/nova-3")

        # Initialize TTS (Text-to-Speech) using LiveKit Inference
        tts = TTS(
            model="cartesia/sonic-3",
            voice="9626c31c-bec5-4cca-baa8-f8ba9e84c8bc",  # British/American female voice
        )

        # Initialize LLM (Language Model) using LiveKit Inference
        llm = LLM(
            model="openai/gpt-4o-mini",
        )

        # Initialize parent class with the instructions and plugins
        super().__init__(
            instructions=instructions,
            stt=stt,
            tts=tts,
            llm=llm,
        )

    async def _publish_tool_status(self, tool_name: str, status: str, message: str):
        """Helper to publish tool call status over the room data channel."""
        if hasattr(self, "room") and self.room:
            try:
                payload = json.dumps({
                    "tool": tool_name,
                    "status": status,
                    "message": message
                })
                await self.room.local_participant.publish_data(payload, topic="tool_call")
            except Exception as e:
                print(f"Error publishing tool status for {tool_name}: {e}")

    @function_tool
    async def identify_user(self, name: str, phone: str) -> str:
        """Identify the patient by collecting their name and phone number. Use this at the start of the call.
        
        Args:
            name: Patient's full name
            phone: Patient's phone number (digits only)
        """
        await self._publish_tool_status("identify_user", "started", "Identifying patient...")
        db = get_db()

        # Check if user exists
        user = db.fetchone("SELECT id FROM users WHERE phone = ?", (phone,))

        if user:
            user_id = user["id"]
            # Update name if provided
            db.execute("UPDATE users SET name = ? WHERE id = ?", (name, user_id))
        else:
            # Create new user
            cursor = db.execute(
                "INSERT INTO users (name, phone) VALUES (?, ?)",
                (name, phone),
            )
            user_id = cursor.lastrowid

        self.state.user_id = user_id
        self.state.user_name = name
        self.state.user_phone = phone

        await self._publish_tool_status("identify_user", "completed", f"Patient identified: {name} ✅")
        
        # Publish user identified event to room
        if hasattr(self, "room") and self.room:
            try:
                user_payload = json.dumps({
                    "user_id": user_id,
                    "name": name,
                    "phone": phone
                })
                await self.room.local_participant.publish_data(user_payload, topic="user_identified")
            except Exception as e:
                print(f"Error publishing user_identified event: {e}")

        return f"User identified: {name} ({phone}). User ID: {user_id}"

    @function_tool
    async def fetch_slots(self, date: str) -> str:
        """Get available appointment slots for a specific date, including the doctor name and specialty.
        
        Args:
            date: Date in YYYY-MM-DD format (e.g., 2026-06-23)
        """
        await self._publish_tool_status("fetch_slots", "started", "Checking available slots...")
        self.state.extracted_date = date

        db = get_db()
        slots = db.fetchall(
            """
            SELECT s.id, s.time, d.name as doctor_name, d.specialty
            FROM time_slots s
            LEFT JOIN doctors d ON s.doctor_id = d.id
            WHERE s.date = ? AND s.available = 1
            ORDER BY s.time, d.name
            """,
            (date,),
        )

        if not slots:
            await self._publish_tool_status("fetch_slots", "completed", "No available slots on this date.")
            return f"No available slots on {date}. Please try another date."

        await self._publish_tool_status("fetch_slots", "completed", "Slots retrieved ✅")
        slots_text = ", ".join([f"{s['time']} with {s['doctor_name']} ({s['specialty']}) (ID: {s['id']})" for s in slots])
        return f"Available slots on {date}: {slots_text}"

    @function_tool
    async def book_appointment(self, user_id: int, slot_id: int) -> str:
        """Book an appointment for the patient.
        
        Args:
            user_id: Patient's ID (from identify_user)
            slot_id: Appointment slot ID (from fetch_slots)
        """
        await self._publish_tool_status("book_appointment", "started", "Booking appointment...")
        db = get_db()

        try:
            # Get slot details
            slot = db.fetchone(
                """
                SELECT s.date, s.time, d.name as doctor_name
                FROM time_slots s
                LEFT JOIN doctors d ON s.doctor_id = d.id
                WHERE s.id = ?
                """,
                (slot_id,),
            )
            if not slot:
                await self._publish_tool_status("book_appointment", "failed", "Slot not found.")
                return "Slot not found."

            # Check if slot is still available (prevent double-booking)
            available = db.fetchone(
                "SELECT available FROM time_slots WHERE id = ?",
                (slot_id,),
            )
            if not available["available"]:
                await self._publish_tool_status("book_appointment", "failed", "Slot already booked.")
                return "This slot was just booked by another call. Please choose another slot."

            # Book appointment
            cursor = db.execute(
                "INSERT INTO appointments (user_id, slot_id, status) VALUES (?, ?, 'booked')",
                (user_id, slot_id),
            )
            appointment_id = cursor.lastrowid

            # Mark slot as unavailable
            db.execute(
                "UPDATE time_slots SET available = 0, booked_at = CURRENT_TIMESTAMP WHERE id = ?",
                (slot_id,),
            )

            self.state.booked_slot_id = slot_id

            await self._publish_tool_status("book_appointment", "completed", "Booking confirmed ✅")
            return (
                f"Appointment booked successfully! "
                f"Date: {slot['date']}, Time: {slot['time']} with {slot['doctor_name']}. "
                f"Appointment ID: {appointment_id}"
            )
        except Exception as e:
            await self._publish_tool_status("book_appointment", "failed", "Error booking slot.")
            return f"Error booking appointment: {str(e)}"

    @function_tool
    async def retrieve_appointments(self, user_id: int) -> str:
        """Get all appointments for a patient.
        
        Args:
            user_id: Patient's ID
        """
        await self._publish_tool_status("retrieve_appointments", "started", "Retrieving appointments...")
        db = get_db()
        appointments = db.fetchall(
            """
            SELECT a.id, a.status, s.date, s.time, d.name as doctor_name
            FROM appointments a
            JOIN time_slots s ON a.slot_id = s.id
            LEFT JOIN doctors d ON s.doctor_id = d.id
            WHERE a.user_id = ? AND a.status != 'cancelled'
            ORDER BY s.date, s.time
            """,
            (user_id,),
        )

        if not appointments:
            await self._publish_tool_status("retrieve_appointments", "completed", "No upcoming appointments.")
            return "No upcoming appointments found."

        await self._publish_tool_status("retrieve_appointments", "completed", "Appointments loaded ✅")
        appts_text = "\n".join(
            [f"- {a['date']} at {a['time']} with {a['doctor_name']} (ID: {a['id']})" for a in appointments]
        )
        return f"Your appointments:\n{appts_text}"

    @function_tool
    async def cancel_appointment(self, appointment_id: int) -> str:
        """Cancel an existing appointment.
        
        Args:
            appointment_id: Appointment ID to cancel
        """
        await self._publish_tool_status("cancel_appointment", "started", "Cancelling appointment...")
        db = get_db()

        try:
            appointment = db.fetchone(
                "SELECT slot_id FROM appointments WHERE id = ?",
                (appointment_id,),
            )
            if not appointment:
                await self._publish_tool_status("cancel_appointment", "failed", "Appointment not found.")
                return "Appointment not found."

            # Cancel appointment
            db.execute(
                "UPDATE appointments SET status = 'cancelled', cancelled_at = CURRENT_TIMESTAMP WHERE id = ?",
                (appointment_id,),
            )

            # Free up the slot
            db.execute(
                "UPDATE time_slots SET available = 1, booked_at = NULL WHERE id = ?",
                (appointment["slot_id"],),
            )

            await self._publish_tool_status("cancel_appointment", "completed", "Appointment cancelled ✅")
            return f"Appointment {appointment_id} has been cancelled."
        except Exception as e:
            await self._publish_tool_status("cancel_appointment", "failed", "Error cancelling appointment.")
            return f"Error cancelling appointment: {str(e)}"

    @function_tool
    async def modify_appointment(self, appointment_id: int, new_slot_id: int) -> str:
        """Reschedule an appointment to a different time.
        
        Args:
            appointment_id: Appointment ID to modify
            new_slot_id: New slot ID
        """
        await self._publish_tool_status("modify_appointment", "started", "Rescheduling appointment...")
        db = get_db()

        try:
            # Get old slot
            appointment = db.fetchone(
                "SELECT slot_id FROM appointments WHERE id = ?",
                (appointment_id,),
            )
            if not appointment:
                await self._publish_tool_status("modify_appointment", "failed", "Appointment not found.")
                return "Appointment not found."

            # Get new slot details
            new_slot = db.fetchone(
                "SELECT date, time, available FROM time_slots WHERE id = ?",
                (new_slot_id,),
            )
            if not new_slot or not new_slot["available"]:
                await self._publish_tool_status("modify_appointment", "failed", "New slot not available.")
                return "New slot is not available."

            # Update appointment
            db.execute(
                "UPDATE appointments SET slot_id = ? WHERE id = ?",
                (new_slot_id, appointment_id),
            )

            # Free old slot
            db.execute(
                "UPDATE time_slots SET available = 1, booked_at = NULL WHERE id = ?",
                (appointment["slot_id"],),
            )

            # Book new slot
            db.execute(
                "UPDATE time_slots SET available = 0, booked_at = CURRENT_TIMESTAMP WHERE id = ?",
                (new_slot_id,),
            )

            await self._publish_tool_status("modify_appointment", "completed", "Rescheduled successfully ✅")
            return f"Appointment rescheduled to {new_slot['date']} at {new_slot['time']}."
        except Exception as e:
            await self._publish_tool_status("modify_appointment", "failed", "Error modifying appointment.")
            return f"Error modifying appointment: {str(e)}"

    @function_tool
    async def end_conversation(self) -> str:
        """End the call and generate a summary. Use this when the patient is ready to hang up."""
        await self._publish_tool_status("end_conversation", "started", "Ending conversation...")
        # Generate summary
        summary = self._generate_summary()

        # Store summary in database
        db = get_db()
        db.execute(
            "INSERT OR REPLACE INTO call_summaries (call_id, summary) VALUES (?, ?)",
            (self.state.call_id, summary),
        )

        print(f"\n[SUMMARY]\n{summary}\n")

        # Publish call_ended event to room
        if hasattr(self, "room") and self.room:
            try:
                payload = json.dumps({"call_id": self.state.call_id})
                await self.room.local_participant.publish_data(payload, topic="call_ended")
            except Exception as e:
                print(f"Error publishing call_ended event: {e}")

        await self._publish_tool_status("end_conversation", "completed", "Consultation completed ✅")
        return "Call summary saved. Session ended."

    def _generate_summary(self) -> str:
        """Generate a summary of the conversation."""
        lines = [
            "## Call Summary",
            f"\n**Patient Information:**",
            f"- Name: {self.state.user_name or 'Not provided'}",
            f"- Phone: {self.state.user_phone or 'Not provided'}",
            f"\n**Actions Taken:**",
        ]

        if self.state.booked_slot_id:
            db = get_db()
            slot = db.fetchone(
                "SELECT date, time FROM time_slots WHERE id = ?",
                (self.state.booked_slot_id,),
            )
            if slot:
                lines.append(f"- Appointment booked for {slot['date']} at {slot['time']}")

        lines.extend([
            f"\n**Call Duration:**",
            f"- Started: {self.state.started_at.strftime('%Y-%m-%d %H:%M:%S')}",
            f"- Total messages: {self.state.message_count}",
        ])

        return "\n".join(lines)

    def _store_conversation(self, role: str, content: str):
        """Store conversation message in database."""
        db = get_db()
        db.execute(
            "INSERT INTO conversation_history (call_id, role, content) VALUES (?, ?, ?)",
            (self.state.call_id, role, content),
        )
