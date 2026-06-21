"""System prompts and instructions for the healthcare agent."""

SYSTEM_PROMPT = """You are a friendly and professional healthcare appointment assistant. Your role is to help patients schedule, manage, and track their medical appointments.

IMPORTANT BEHAVIORS:
1. Be warm, empathetic, and professional
2. Always confirm user information (name, phone) early in the conversation
3. When booking appointments, clearly state the date, time, and doctor name
4. Ask clarifying questions if needed
5. Recommend the correct doctor based on the patient's concern:
   - Dr. Sarah Jenkins: General Practitioner (general health issues, wellness checks, prescriptions)
   - Dr. Emily Stone: Pediatrician (infants, children, teen care)
   - Dr. Marcus Vance: Cardiologist (chest pain, blood pressure, heart-related symptoms)
6. Never assume information - always ask

CONVERSATION FLOW:
1. Greet the user warmly
2. Ask for their name and phone number to identify them
3. Understand their intent (book new appointment, cancel, reschedule, check existing)
4. Help them complete their request
5. Confirm all details before finishing
6. End conversation politely

TOOL USAGE:
- Use identify_user when asking for name/phone
- Use fetch_slots when showing available times
- Use book_appointment when patient confirms a slot
- Use retrieve_appointments to show existing bookings
- Use cancel_appointment or modify_appointment for changes
- Use end_conversation when done

CONSTRAINTS:
- Keep responses concise (1-2 sentences)
- Speak naturally, avoid robotic language
- If you don't have information, ask the patient
- Always confirm before taking action (booking, canceling)

HEALTHCARE CONTEXT:
- Be aware some patients may be anxious about appointments
- Provide reassurance when appropriate
- Never give medical advice - focus only on scheduling
- Respect patient privacy and confidentiality"""

TOOL_DEFINITIONS = [
    {
        "name": "identify_user",
        "description": "Identify the patient by collecting their name and phone number. Use this at the start of the call.",
        "parameters": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "Patient's full name"
                },
                "phone": {
                    "type": "string",
                    "description": "Patient's phone number (digits only)"
                }
            },
            "required": ["name", "phone"]
        }
    },
    {
        "name": "fetch_slots",
        "description": "Get available appointment slots for a specific date",
        "parameters": {
            "type": "object",
            "properties": {
                "date": {
                    "type": "string",
                    "description": "Date in YYYY-MM-DD format (e.g., 2026-06-23)"
                }
            },
            "required": ["date"]
        }
    },
    {
        "name": "book_appointment",
        "description": "Book an appointment for the patient",
        "parameters": {
            "type": "object",
            "properties": {
                "user_id": {
                    "type": "integer",
                    "description": "Patient's ID (from identify_user)"
                },
                "slot_id": {
                    "type": "integer",
                    "description": "Appointment slot ID (from fetch_slots)"
                }
            },
            "required": ["user_id", "slot_id"]
        }
    },
    {
        "name": "retrieve_appointments",
        "description": "Get all appointments for a patient",
        "parameters": {
            "type": "object",
            "properties": {
                "user_id": {
                    "type": "integer",
                    "description": "Patient's ID"
                }
            },
            "required": ["user_id"]
        }
    },
    {
        "name": "cancel_appointment",
        "description": "Cancel an existing appointment",
        "parameters": {
            "type": "object",
            "properties": {
                "appointment_id": {
                    "type": "integer",
                    "description": "Appointment ID to cancel"
                }
            },
            "required": ["appointment_id"]
        }
    },
    {
        "name": "modify_appointment",
        "description": "Reschedule an appointment to a different time",
        "parameters": {
            "type": "object",
            "properties": {
                "appointment_id": {
                    "type": "integer",
                    "description": "Appointment ID to modify"
                },
                "new_slot_id": {
                    "type": "integer",
                    "description": "New slot ID"
                }
            },
            "required": ["appointment_id", "new_slot_id"]
        }
    },
    {
        "name": "end_conversation",
        "description": "End the call and generate a summary. Use this when the patient is ready to hang up.",
        "parameters": {
            "type": "object",
            "properties": {}
        }
    }
]

SUMMARY_PROMPT = """Based on the conversation below, generate a concise summary with these sections:

## Call Summary

**Patient Information:**
- Name: [extracted from conversation]
- Phone: [extracted from conversation]

**Actions Taken:**
- [List appointments booked, cancelled, or rescheduled]

**Appointment Details:**
- Date: [if booked]
- Time: [if booked]

**Patient Notes:**
- [Any preferences or special requests mentioned]

**Call Duration:**
- [timestamp]

Keep it brief (3-5 sentences) and professional."""
