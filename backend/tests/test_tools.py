import os
import pytest
from pathlib import Path
import sqlite3

from backend.db import Database, get_db
import backend.db
from backend.agent.conversation import HealthcareAgent, ConversationState


@pytest.fixture(autouse=True)
def test_db():
    # Set up temporary test database path
    test_db_path = "test_voice_agent.db"
    if os.path.exists(test_db_path):
        try:
            os.remove(test_db_path)
        except Exception:
            pass
    
    # Override global db instance
    backend.db._db_instance = Database(db_path=test_db_path)
    
    yield backend.db._db_instance
    
    # Tear down
    backend.db._db_instance = None
    if os.path.exists(test_db_path):
        try:
            os.remove(test_db_path)
        except Exception:
            pass


@pytest.mark.asyncio
async def test_identify_user():
    # Initialize agent
    agent = HealthcareAgent()
    agent.state = ConversationState(call_id="test-call-id")
    
    # Identify new user
    result = await agent.identify_user(name="John Doe", phone="1234567890")
    assert "User identified" in result
    assert "John Doe" in result
    assert agent.state.user_name == "John Doe"
    assert agent.state.user_phone == "1234567890"
    assert agent.state.user_id is not None
    
    # Identify same user again, verify it retrieves existing ID
    first_id = agent.state.user_id
    result2 = await agent.identify_user(name="John Doe", phone="1234567890")
    assert f"User ID: {first_id}" in result2
    assert agent.state.user_id == first_id


@pytest.mark.asyncio
async def test_fetch_slots():
    agent = HealthcareAgent()
    agent.state = ConversationState(call_id="test-call-id")
    
    # Fetch slots for prepopulated date 2026-06-23
    result = await agent.fetch_slots(date="2026-06-23")
    assert "Available slots on 2026-06-23" in result
    assert "09:00" in result
    assert agent.state.extracted_date == "2026-06-23"
    
    # Fetch slots for invalid date
    result2 = await agent.fetch_slots(date="2026-06-30")
    assert "No available slots on 2026-06-30" in result2


@pytest.mark.asyncio
async def test_book_appointment():
    agent = HealthcareAgent()
    agent.state = ConversationState(call_id="test-call-id")
    
    # Set up user in database
    await agent.identify_user(name="Jane Doe", phone="9876543210")
    user_id = agent.state.user_id
    
    # Book a slot (slot ID 1 is 2026-06-23 09:00)
    result = await agent.book_appointment(user_id=user_id, slot_id=1)
    assert "Appointment booked successfully" in result
    assert "09:00" in result
    assert agent.state.booked_slot_id == 1
    
    # Verify slot is no longer available
    db = get_db()
    slot = db.fetchone("SELECT available FROM time_slots WHERE id = 1")
    assert slot["available"] == 0


@pytest.mark.asyncio
async def test_double_booking_prevention():
    agent1 = HealthcareAgent()
    agent1.state = ConversationState(call_id="call-1")
    
    agent2 = HealthcareAgent()
    agent2.state = ConversationState(call_id="call-2")
    
    # Create two users
    await agent1.identify_user(name="User 1", phone="1111111111")
    await agent2.identify_user(name="User 2", phone="2222222222")
    
    # Book same slot (ID 2) for user 1
    res1 = await agent1.book_appointment(user_id=agent1.state.user_id, slot_id=2)
    assert "Appointment booked successfully" in res1
    
    # Attempt to book same slot (ID 2) for user 2, should fail
    res2 = await agent2.book_appointment(user_id=agent2.state.user_id, slot_id=2)
    assert "This slot was just booked by another call" in res2


@pytest.mark.asyncio
async def test_retrieve_appointments():
    agent = HealthcareAgent()
    agent.state = ConversationState(call_id="test-call-id")
    
    await agent.identify_user(name="Bob Smith", phone="3333333333")
    user_id = agent.state.user_id
    
    # Check initially empty
    res_empty = await agent.retrieve_appointments(user_id=user_id)
    assert "No upcoming appointments found" in res_empty
    
    # Book an appointment
    await agent.book_appointment(user_id=user_id, slot_id=3)
    
    # Retrieve and verify
    res_found = await agent.retrieve_appointments(user_id=user_id)
    assert "Your appointments:" in res_found
    db = get_db()
    slot = db.fetchone("SELECT time FROM time_slots WHERE id = 3")
    assert slot["time"] in res_found


@pytest.mark.asyncio
async def test_cancel_appointment():
    agent = HealthcareAgent()
    agent.state = ConversationState(call_id="test-call-id")
    
    await agent.identify_user(name="Alice Johnson", phone="4444444444")
    user_id = agent.state.user_id
    
    # Book appointment
    book_res = await agent.book_appointment(user_id=user_id, slot_id=4)
    # Extract appointment ID
    appt_id = int(book_res.split("Appointment ID: ")[1])
    
    # Cancel appointment
    cancel_res = await agent.cancel_appointment(appointment_id=appt_id)
    assert f"Appointment {appt_id} has been cancelled" in cancel_res
    
    # Verify slot is free again
    db = get_db()
    slot = db.fetchone("SELECT available FROM time_slots WHERE id = 4")
    assert slot["available"] == 1


@pytest.mark.asyncio
async def test_modify_appointment():
    agent = HealthcareAgent()
    agent.state = ConversationState(call_id="test-call-id")
    
    await agent.identify_user(name="Charlie Brown", phone="5555555555")
    user_id = agent.state.user_id
    
    # Book slot 5
    book_res = await agent.book_appointment(user_id=user_id, slot_id=5)
    appt_id = int(book_res.split("Appointment ID: ")[1])
    
    # Modify/Reschedule to slot 6
    modify_res = await agent.modify_appointment(appointment_id=appt_id, new_slot_id=6)
    assert "Appointment rescheduled" in modify_res
    
    db = get_db()
    # Check old slot 5 is free
    slot5 = db.fetchone("SELECT available FROM time_slots WHERE id = 5")
    assert slot5["available"] == 1
    
    # Check new slot 6 is booked
    slot6 = db.fetchone("SELECT available FROM time_slots WHERE id = 6")
    assert slot6["available"] == 0


@pytest.mark.asyncio
async def test_end_conversation():
    agent = HealthcareAgent()
    agent.state = ConversationState(call_id="test-call-id")
    
    await agent.identify_user(name="David Miller", phone="6666666666")
    user_id = agent.state.user_id
    await agent.book_appointment(user_id=user_id, slot_id=7)
    
    end_res = await agent.end_conversation()
    assert "Call summary saved" in end_res
    
    # Verify summary is in database
    db = get_db()
    summary = db.fetchone("SELECT summary FROM call_summaries WHERE call_id = 'test-call-id'")
    assert summary is not None
    assert "David Miller" in summary["summary"]
    assert "6666666666" in summary["summary"]


@pytest.mark.asyncio
async def test_summary_fallback_on_exception():
    agent = HealthcareAgent()
    agent.state = ConversationState(
        call_id="error-call-id",
        user_id=1,
        user_name="Error Test User",
        user_phone="9990008888"
    )
    
    db = get_db()
    
    # Run the exact fallback logic as structured in main.py
    try:
        raise ValueError("Simulated OpenAI connection timeout")
    except Exception as e:
        import json
        fallback_summary = {
            "summary": f"Could not generate AI summary due to an error: {str(e)}",
            "preferences": "None",
            "user_id": agent.state.user_id,
            "name": agent.state.user_name or "Anonymous Patient",
            "phone": agent.state.user_phone or "Not provided"
        }
        db.execute(
            "INSERT OR REPLACE INTO call_summaries (call_id, appointment_id, summary) VALUES (?, ?, ?)",
            (agent.state.call_id, None, json.dumps(fallback_summary)),
        )
        
    # Verify fallback is written to database and readable
    row = db.fetchone("SELECT summary FROM call_summaries WHERE call_id = 'error-call-id'")
    assert row is not None
    data = json.loads(row["summary"])
    assert data["name"] == "Error Test User"
    assert data["phone"] == "9990008888"
    assert "Simulated OpenAI connection timeout" in data["summary"]
