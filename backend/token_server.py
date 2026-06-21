import os
import json
from aiohttp import web
from dotenv import load_dotenv
from livekit import api
from backend.db import get_db

load_dotenv()


# ALLOWED_ORIGIN: set this env var on Render to your Vercel frontend URL
# e.g. https://carevoice-ai.vercel.app
# Defaults to * for local development only
ALLOWED_ORIGIN = os.getenv("ALLOWED_ORIGIN", "*")


def cors_headers():
    return {
        "Access-Control-Allow-Origin": ALLOWED_ORIGIN,
        "Access-Control-Allow-Headers": "Content-Type, Authorization",
        "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
    }


async def handle_options(request):
    return web.Response(headers=cors_headers())


async def get_token(request):
    room = request.query.get("room")
    identity = request.query.get("identity", "patient-user")
    phone = request.query.get("phone", "")

    if not room:
        return web.json_response({"error": "room parameter is required"}, status=400, headers=cors_headers())

    api_key = os.getenv("LIVEKIT_API_KEY")
    api_secret = os.getenv("LIVEKIT_API_SECRET")

    if not api_key or not api_secret:
        return web.json_response({"error": "LIVEKIT_API_KEY and LIVEKIT_API_SECRET must be set"}, status=500, headers=cors_headers())

    # Pack metadata as JSON string containing name and phone
    metadata_str = json.dumps({
        "name": identity,
        "phone": phone
    })

    grants = api.VideoGrants(room_join=True, room=room)
    token = (
        api.AccessToken(api_key, api_secret)
        .with_identity(identity)
        .with_name(identity)
        .with_metadata(metadata_str)
        .with_grants(grants)
    )

    return web.json_response({"token": token.to_jwt()}, headers=cors_headers())


async def identify_user(request):
    try:
        body = await request.json()
        name = body.get("name")
        phone = body.get("phone")
    except Exception:
        return web.json_response({"error": "Invalid JSON"}, status=400, headers=cors_headers())

    if not name or not phone:
        return web.json_response({"error": "name and phone are required"}, status=400, headers=cors_headers())

    db = get_db()
    user = db.fetchone("SELECT id, name, phone FROM users WHERE phone = ?", (phone,))

    if user:
        user_id = user["id"]
        db.execute("UPDATE users SET name = ? WHERE id = ?", (name, user_id))
    else:
        cursor = db.execute("INSERT INTO users (name, phone) VALUES (?, ?)", (name, phone))
        user_id = cursor.lastrowid

    return web.json_response({
        "user_id": user_id,
        "name": name,
        "phone": phone
    }, headers=cors_headers())


async def get_slots(request):
    date = request.query.get("date")
    if not date:
        return web.json_response({"error": "date is required"}, status=400, headers=cors_headers())

    db = get_db()
    slots = db.fetchall(
        """
        SELECT s.id, s.time, s.available, d.name as doctor_name, d.specialty as doctor_specialty
        FROM time_slots s
        LEFT JOIN doctors d ON s.doctor_id = d.id
        WHERE s.date = ?
        ORDER BY s.time, d.name
        """,
        (date,),
    )

    result = [{
        "id": s["id"],
        "time": s["time"],
        "available": bool(s["available"]),
        "doctor_name": s["doctor_name"],
        "doctor_specialty": s["doctor_specialty"]
    } for s in slots]
    return web.json_response({"slots": result}, headers=cors_headers())


async def get_appointments(request):
    phone = request.query.get("phone")
    if not phone:
        return web.json_response({"error": "phone is required"}, status=400, headers=cors_headers())

    db = get_db()
    user = db.fetchone("SELECT id FROM users WHERE phone = ?", (phone,))
    if not user:
        return web.json_response({"appointments": []}, headers=cors_headers())

    appointments = db.fetchall(
        """
        SELECT a.id, a.status, s.id as slot_id, s.date, s.time, d.name as doctor_name, d.specialty as doctor_specialty
        FROM appointments a
        JOIN time_slots s ON a.slot_id = s.id
        LEFT JOIN doctors d ON s.doctor_id = d.id
        WHERE a.user_id = ? AND a.status != 'cancelled'
        ORDER BY s.date, s.time
        """,
        (user["id"],),
    )

    result = [{
        "id": a["id"],
        "slot_id": a["slot_id"],
        "date": a["date"],
        "time": a["time"],
        "status": a["status"],
        "doctor_name": a["doctor_name"],
        "doctor_specialty": a["doctor_specialty"]
    } for a in appointments]

    return web.json_response({"appointments": result}, headers=cors_headers())


async def cancel_appointment(request):
    try:
        body = await request.json()
        appointment_id = body.get("appointment_id")
    except Exception:
        return web.json_response({"error": "Invalid JSON"}, status=400, headers=cors_headers())

    if not appointment_id:
        return web.json_response({"error": "appointment_id is required"}, status=400, headers=cors_headers())

    db = get_db()
    try:
        appointment = db.fetchone(
            "SELECT slot_id FROM appointments WHERE id = ?",
            (appointment_id,),
        )
        if not appointment:
            return web.json_response({"error": "Appointment not found"}, status=404, headers=cors_headers())

        db.execute(
            "UPDATE appointments SET status = 'cancelled', cancelled_at = CURRENT_TIMESTAMP WHERE id = ?",
            (appointment_id,),
        )
        db.execute(
            "UPDATE time_slots SET available = 1, booked_at = NULL WHERE id = ?",
            (appointment["slot_id"],),
        )

        return web.json_response({"message": f"Appointment {appointment_id} cancelled"}, headers=cors_headers())
    except Exception as e:
        return web.json_response({"error": str(e)}, status=500, headers=cors_headers())


async def modify_appointment(request):
    try:
        body = await request.json()
        appointment_id = body.get("appointment_id")
        new_slot_id = body.get("new_slot_id")
    except Exception:
        return web.json_response({"error": "Invalid JSON"}, status=400, headers=cors_headers())

    if not appointment_id or not new_slot_id:
        return web.json_response({"error": "appointment_id and new_slot_id are required"}, status=400, headers=cors_headers())

    db = get_db()
    try:
        appointment = db.fetchone(
            "SELECT slot_id FROM appointments WHERE id = ?",
            (appointment_id,),
        )
        if not appointment:
            return web.json_response({"error": "Appointment not found"}, status=404, headers=cors_headers())

        new_slot = db.fetchone(
            "SELECT available FROM time_slots WHERE id = ?",
            (new_slot_id,),
        )
        if not new_slot or not new_slot["available"]:
            return web.json_response({"error": "New slot not available"}, status=400, headers=cors_headers())

        db.execute(
            "UPDATE appointments SET slot_id = ? WHERE id = ?",
            (new_slot_id, appointment_id),
        )
        db.execute(
            "UPDATE time_slots SET available = 1, booked_at = NULL WHERE id = ?",
            (appointment["slot_id"],),
        )
        db.execute(
            "UPDATE time_slots SET available = 0, booked_at = CURRENT_TIMESTAMP WHERE id = ?",
            (new_slot_id,),
        )

        return web.json_response({"message": "Appointment modified successfully"}, headers=cors_headers())
    except Exception as e:
        return web.json_response({"error": str(e)}, status=500, headers=cors_headers())


async def get_call_summary(request):
    call_id = request.query.get("call_id")
    if not call_id:
        return web.json_response({"error": "call_id is required"}, status=400, headers=cors_headers())

    db = get_db()
    row = db.fetchone(
        "SELECT summary, generated_at FROM call_summaries WHERE call_id = ?",
        (call_id,)
    )

    if not row:
        return web.json_response({"status": "pending"}, status=404, headers=cors_headers())

    try:
        summary_data = json.loads(row["summary"])
    except Exception:
        summary_data = {"summary": row["summary"], "preferences": "None"}

    phone = summary_data.get("phone")
    appointments = []
    
    if phone:
        # Fetch active appointments for this phone
        user = db.fetchone("SELECT id FROM users WHERE phone = ?", (phone,))
        if user:
            appts = db.fetchall(
                """
                SELECT a.id, a.status, s.id as slot_id, s.date, s.time, d.name as doctor_name, d.specialty as doctor_specialty
                FROM appointments a
                JOIN time_slots s ON a.slot_id = s.id
                LEFT JOIN doctors d ON s.doctor_id = d.id
                WHERE a.user_id = ? AND a.status != 'cancelled'
                ORDER BY s.date, s.time
                """,
                (user["id"],),
            )
            appointments = [{
                "id": a["id"],
                "slot_id": a["slot_id"],
                "date": a["date"],
                "time": a["time"],
                "status": a["status"],
                "doctor_name": a["doctor_name"],
                "doctor_specialty": a["doctor_specialty"]
            } for a in appts]

    timestamp_str = row["generated_at"]
    if timestamp_str and "Z" not in timestamp_str and "+" not in timestamp_str:
        timestamp_str = timestamp_str.replace(" ", "T") + "Z"

    response_data = {
        "status": "completed",
        "summary": summary_data.get("summary", ""),
        "preferences": summary_data.get("preferences", "None"),
        "user": {
            "user_id": summary_data.get("user_id"),
            "name": summary_data.get("name", "Anonymous"),
            "phone": phone or "Not provided"
        },
        "appointments": appointments,
        "timestamp": timestamp_str
    }
    
    return web.json_response(response_data, headers=cors_headers())


async def book_appointment_api(request):
    try:
        body = await request.json()
        user_id = body.get("user_id")
        slot_id = body.get("slot_id")
    except Exception:
        return web.json_response({"error": "Invalid JSON"}, status=400, headers=cors_headers())

    if not user_id or not slot_id:
        return web.json_response({"error": "user_id and slot_id are required"}, status=400, headers=cors_headers())

    db = get_db()
    try:
        slot = db.fetchone("SELECT available FROM time_slots WHERE id = ?", (slot_id,))
        if not slot or not slot["available"]:
            return web.json_response({"error": "Slot not available"}, status=400, headers=cors_headers())

        db.execute(
            "INSERT INTO appointments (user_id, slot_id, status) VALUES (?, ?, 'booked')",
            (user_id, slot_id),
        )
        db.execute(
            "UPDATE time_slots SET available = 0, booked_at = CURRENT_TIMESTAMP WHERE id = ?",
            (slot_id,),
        )
        return web.json_response({"message": "Appointment booked successfully"}, headers=cors_headers())
    except Exception as e:
        return web.json_response({"error": str(e)}, status=500, headers=cors_headers())


app = web.Application()
app.router.add_get("/token", get_token)
app.router.add_post("/api/identify", identify_user)
app.router.add_get("/api/slots", get_slots)
app.router.add_get("/api/appointments", get_appointments)
app.router.add_post("/api/appointments/cancel", cancel_appointment)
app.router.add_post("/api/appointments/modify", modify_appointment)
app.router.add_get("/api/summary", get_call_summary)
app.router.add_post("/api/appointments/book", book_appointment_api)

# Add options catch-alls for pre-flight requests
app.router.add_options("/{tail:.*}", handle_options)

if __name__ == "__main__":
    web.run_app(app, port=8080)
