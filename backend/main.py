#!/usr/bin/env python3
"""
Main entry point for the Voice AI Agent.
Orchestrates LiveKit connection and agent setup using LiveKit Agents 1.x.
"""

import asyncio
import logging
from livekit.agents import (
    JobContext,
    JobProcess,
    WorkerOptions,
    cli,
    AgentSession,
    TurnHandlingOptions,
    inference,
    ConversationItemAddedEvent,
    ChatMessage
)

from backend.config import Config
from backend.agent import HealthcareAgent
from livekit.plugins import tavus

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


def prewarm(proc: JobProcess):
    """Prewarm the agent process."""
    logger.info("Prewarming agent process...")


async def entrypoint(ctx: JobContext):
    """Main entrypoint for the voice agent job."""
    logger.info(f"Starting voice agent job: {ctx.job.id}")

    # Connect to the room
    await ctx.connect()
    logger.info(f"Connected to room: {ctx.room.name}")

    # Extract user metadata from participants if present
    patient_name = None
    patient_phone = None
    user_id = None

    import json
    from backend.db import get_db
    from backend.agent.prompts import SYSTEM_PROMPT

    for participant in ctx.room.remote_participants.values():
        logger.info(f"Checking participant: {participant.identity}, metadata: {participant.metadata}")
        if participant.metadata:
            try:
                meta = json.loads(participant.metadata)
                patient_name = meta.get("name")
                patient_phone = meta.get("phone")
                logger.info(f"Found patient metadata: name={patient_name}, phone={patient_phone}")
                break
            except Exception as e:
                logger.error(f"Error parsing participant metadata: {e}")

    if patient_phone:
        try:
            db = get_db()
            user = db.fetchone("SELECT id FROM users WHERE phone = ?", (patient_phone,))
            if user:
                user_id = user["id"]
                logger.info(f"Database matched patient ID: {user_id} for phone: {patient_phone}")
        except Exception as e:
            logger.error(f"Error loading user_id from database: {e}")

    # Customize instructions to make agent aware of the identified user and today's date
    from datetime import datetime
    current_date_str = datetime.now().strftime("%Y-%m-%d")
    current_weekday = datetime.now().strftime("%A")

    instructions = SYSTEM_PROMPT + f"\n\nCURRENT TEMPORAL CONTEXT: Today's date is {current_date_str} ({current_weekday}). Always refer to this date as 'today' and use it as the reference point for relative dates like 'tomorrow' or 'next week'."

    if patient_name and patient_phone:
        instructions += (
            f"\n\nCURRENT PATIENT CONTEXT: The user is already identified. "
            f"Their name is '{patient_name}' and their phone number is '{patient_phone}' (User ID: {user_id}). "
            f"DO NOT ask them for their name or phone number. "
            f"Welcome them back warmly by name (e.g. 'Hello {patient_name}, welcome back! how can I help you today?') "
            f"and proceed directly to helping them manage their appointments."
        )

    # Initialize the healthcare agent with preset details
    agent = HealthcareAgent(
        user_id=user_id,
        user_name=patient_name,
        user_phone=patient_phone,
        instructions=instructions,
    )
    # Link the room to the agent for WebRTC data publishing
    agent.room = ctx.room
    logger.info("Healthcare agent initialized")

    # Create the AgentSession
    session = AgentSession(
        stt=agent.stt,
        llm=agent.llm,
        tts=agent.tts,
        turn_handling=TurnHandlingOptions(
            turn_detection=inference.TurnDetector(),
        ),
    )

    # Initialize and start Tavus Avatar Session if credentials are configured
    tavus_api_key = Config.TAVUS_API_KEY
    tavus_replica_id = Config.TAVUS_REPLICA_ID
    tavus_persona_id = Config.TAVUS_PERSONA_ID

    avatar_session = None
    if tavus_api_key and tavus_replica_id:
        try:
            logger.info("Initializing Tavus AvatarSession...")
            avatar_session = tavus.AvatarSession(
                api_key=tavus_api_key,
                replica_id=tavus_replica_id,
                persona_id=tavus_persona_id,
            )
            logger.info("Tavus AvatarSession initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize Tavus AvatarSession: {e}")

    if avatar_session:
        try:
            logger.info("Starting Tavus avatar session...")
            await avatar_session.start(session, room=ctx.room)
            logger.info("Tavus avatar session started successfully")
        except Exception as e:
            logger.error(f"Failed to start Tavus avatar session: {e}. Falling back to audio-only.")
            avatar_session = None

    # Listen to conversation items added to persist history
    @session.on("conversation_item_added")
    def on_item_added(event: ConversationItemAddedEvent):
        item = event.item
        if isinstance(item, ChatMessage):
            if item.role in ("user", "assistant"):
                agent.state.message_count += 1
                agent._store_conversation(item.role, item.text_content)

    # Keep active session and handle final summary generation when cancelled/disconnected
    try:
        logger.info("Starting voice agent session in room...")
        await session.start(room=ctx.room, agent=agent)

        # Send call_id to the room
        try:
            init_payload = json.dumps({"call_id": agent.state.call_id})
            await ctx.room.local_participant.publish_data(init_payload, topic="call_started")
        except Exception as e:
            logger.error(f"Error publishing call_started event: {e}")

        # Generate initial greeting
        greeting_instructions = "Greet the user and offer your assistance."
        if patient_name:
            greeting_instructions = (
                f"Greet the user warmly by name ({patient_name}), welcome them back, and offer your assistance. "
                f"Do NOT ask for their name or phone number since they are already logged in."
            )

        await session.generate_reply(
            instructions=greeting_instructions
        )
        logger.info("Initial greeting generated. Session active.")

        # Wait until room disconnected or job cancelled
        from livekit.rtc import ConnectionState
        while ctx.room.connection_state != ConnectionState.CONN_DISCONNECTED:
            await asyncio.sleep(0.5)

    except asyncio.CancelledError:
        logger.info("Session cancelled/ended.")
    finally:
        logger.info(f"Generating post-call summary for call_id: {agent.state.call_id}...")
        try:
            db = get_db()
            # Fetch all conversation messages
            history = db.fetchall(
                "SELECT role, content FROM conversation_history WHERE call_id = ? ORDER BY id ASC",
                (agent.state.call_id,)
            )

            if history:
                messages = [{"role": h["role"], "content": h["content"]} for h in history]
                summary_prompt = (
                    "Summarize the conversation between a patient and a medical booking assistant. "
                    "Provide a clean JSON response containing exactly two keys:\n"
                    "1. 'summary': A 2-3 sentence summary of the conversation and its outcome.\n"
                    "2. 'preferences': Extracted user preferences if any (e.g. prefers morning slots, pediatrician, or general practitioner). If none, return 'None'.\n\n"
                    "Do not include any markdown format like ```json ... ```, just return the raw JSON object."
                )

                import openai
                client = openai.OpenAI(api_key=Config.OPENAI_API_KEY)
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": summary_prompt},
                        {"role": "user", "content": json.dumps(messages)}
                    ],
                    max_tokens=250,
                    temperature=0.3
                )
                result_text = response.choices[0].message.content.strip()
                if result_text.startswith("```"):
                    lines = result_text.split("\n")
                    if lines[0].startswith("```"):
                        lines = lines[1:]
                    if lines[-1].startswith("```"):
                        lines = lines[:-1]
                    result_text = "\n".join(lines).strip()
                try:
                    summary_data = json.loads(result_text)
                except Exception:
                    summary_data = {
                        "summary": result_text,
                        "preferences": "None"
                    }
            else:
                summary_data = {
                    "summary": "No conversation occurred.",
                    "preferences": "None"
                }

            summary_data["user_id"] = agent.state.user_id
            summary_data["name"] = agent.state.user_name
            summary_data["phone"] = agent.state.user_phone

            # Fetch patient appointments to link if booked
            booked_appt_id = None
            if agent.state.booked_slot_id:
                appt = db.fetchone(
                    "SELECT id FROM appointments WHERE slot_id = ?",
                    (agent.state.booked_slot_id,)
                )
                if appt:
                    booked_appt_id = appt["id"]

            db.execute(
                "INSERT OR REPLACE INTO call_summaries (call_id, appointment_id, summary) VALUES (?, ?, ?)",
                (agent.state.call_id, booked_appt_id, json.dumps(summary_data)),
            )
            logger.info("Call summary saved successfully to database.")
        except Exception as e:
            logger.error(f"Error generating call summary: {e}")
            try:
                error_msg = str(e)
                if "quota" in error_msg.lower() or "429" in error_msg:
                    summary_text = "Consultation completed. (AI summary service temporarily unavailable: OpenAI API quota limits exceeded on this key)."
                else:
                    summary_text = f"Consultation completed. (AI summary generation error: {error_msg})"

                fallback_summary = {
                    "summary": summary_text,
                    "preferences": "None",
                    "user_id": agent.state.user_id,
                    "name": agent.state.user_name or "Anonymous Patient",
                    "phone": agent.state.user_phone or "Not provided"
                }
                booked_appt_id = None
                if agent.state.booked_slot_id:
                    appt = db.fetchone(
                        "SELECT id FROM appointments WHERE slot_id = ?",
                        (agent.state.booked_slot_id,)
                    )
                    if appt:
                        booked_appt_id = appt["id"]
                db.execute(
                    "INSERT OR REPLACE INTO call_summaries (call_id, appointment_id, summary) VALUES (?, ?, ?)",
                    (agent.state.call_id, booked_appt_id, json.dumps(fallback_summary)),
                )
                logger.info("Fallback call summary saved successfully to database.")
            except Exception as db_err:
                logger.error(f"Failed to write fallback summary to database: {db_err}")


def main():
    """Start the agent worker."""
    logger.info("Voice AI Agent Starting...")
    logger.info(f"LiveKit URL: {Config.LIVEKIT_URL}")

    # Validate configuration
    try:
        Config.validate()
        logger.info("Configuration validated successfully")
    except ValueError as e:
        logger.error(f"Configuration error: {e}")
        raise

    # Create worker and run
    worker = WorkerOptions(
        entrypoint_fnc=entrypoint,
        prewarm_fnc=prewarm,
    )

    cli.run_app(worker)


if __name__ == "__main__":
    main()
