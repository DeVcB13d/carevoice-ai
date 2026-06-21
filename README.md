# CareVoice AI 🩺🎙️

> **AI-powered voice agent for medical appointment booking** — talk to an intelligent assistant, book/reschedule/cancel appointments, and get a full call summary with calendar view.

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)](https://python.org)
[![React](https://img.shields.io/badge/React-18-61DAFB?logo=react&logoColor=black)](https://react.dev)
[![LiveKit](https://img.shields.io/badge/LiveKit-Agents-00A699?logo=data:image/svg+xml;base64,)](https://livekit.io)
[![Tavus](https://img.shields.io/badge/Tavus-Avatar-7C3AED)](https://tavus.io)

---

## ✨ Features

| Feature | Description |
|---|---|
| 🎙️ **Voice-First Interface** | Real-time speech-to-text (Deepgram) + text-to-speech (Cartesia) via LiveKit |
| 🤖 **AI Video Avatar** | Tavus-powered photorealistic doctor avatar responds in video |
| 📅 **Calendar Booking** | Visual calendar to browse doctors, select slots, book appointments |
| 🔁 **Session Memory** | Identify by phone number — returning users get their history automatically |
| 📝 **Auto Call Summary** | AI-generated summary with booked appointments, preferences, and timestamps |
| 🛠️ **Live Tool Feedback** | Visual on-screen indicator for every agent tool call ("Fetching slots…", "Booking confirmed ✅") |
| 💬 **Dual Transcript** | Color-coded chat bubbles (you on right, agent on left) |

---

## 🏗️ Architecture

```
┌──────────────────────┐         HTTPS          ┌─────────────────────────┐
│   React Frontend     │ ──────────────────────► │  Python Token Server    │
│   (Vite + TS)        │                         │  (aiohttp :8080)        │
└──────────────────────┘                         └──────────┬──────────────┘
         │                                                   │
         │  WebRTC (LiveKit SDK)                    LiveKit Cloud
         │                                                   │
         └─────────────────────────────────────────────────► │
                                                   ┌──────────▼──────────────┐
                                                   │  Python Agent Worker    │
                                                   │  (LiveKit Agents 1.x)   │
                                                   │                         │
                                                   │  STT: Deepgram          │
                                                   │  LLM: OpenAI GPT-4o     │
                                                   │  TTS: Cartesia          │
                                                   │  Avatar: Tavus          │
                                                   └──────────┬──────────────┘
                                                              │ SQLite
                                                   ┌──────────▼──────────────┐
                                                   │  voice_agent.db         │
                                                   │  users · appointments   │
                                                   │  time_slots · summaries │
                                                   └─────────────────────────┘
```

### Key Files

```
carevoice-ai/
├── backend/
│   ├── main.py               # Agent worker entrypoint (LiveKit job)
│   ├── token_server.py       # HTTP API server (token, appointments, summary)
│   ├── config.py             # Environment config loader
│   ├── agent/
│   │   ├── conversation.py   # HealthcareAgent class + all tool definitions
│   │   └── prompts.py        # System prompt for the LLM
│   └── db/
│       ├── schema.sql        # Database schema
│       └── __init__.py       # DB helper (fetchone / fetchall / execute)
├── frontend/
│   └── src/
│       └── App.tsx           # Main React app (LiveKit room, calendar, summary)
├── requirements.txt
├── .env.example              # ← copy to .env and fill in your keys
└── ARCHITECTURE.md           # Detailed system design notes
```

---

## 🚀 Quick Start (Local Development)

### Prerequisites
- Python 3.11+
- Node.js 18+
- Accounts for: [LiveKit Cloud](https://livekit.io), [Tavus](https://tavus.io), [OpenAI](https://platform.openai.com), [Deepgram](https://console.deepgram.com)

### 1. Clone & set up environment

```bash
git clone https://github.com/DeVcB13d/carevoice-ai.git
cd carevoice-ai

# Copy and fill in your API keys
cp .env.example .env
# Edit .env with your actual keys
```

### 2. Backend setup

```bash
# Create virtual environment
python -m venv .venv

# Activate (Windows)
.venv\Scripts\activate

# Activate (Mac/Linux)
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Initialise the database (creates voice_agent.db with schema + seed data)
python -c "from backend.db import init_db; init_db()"
```

### 3. Start the backend services

Open **two terminals**:

**Terminal 1 — Token Server (REST API)**
```bash
python -m backend.token_server
# Starts on http://localhost:8080
```

**Terminal 2 — Agent Worker**
```bash
python -m backend.main dev
# Connects to LiveKit Cloud and waits for room assignments
```

### 4. Frontend setup

```bash
cd frontend
npm install
npm run dev
# Opens on http://localhost:5173
```

Open `http://localhost:5173` in your browser, click **Start Call**, and speak!

---

## ⚙️ Environment Variables

Copy `.env.example` to `.env` and fill in:

| Variable | Required | Description |
|---|---|---|
| `LIVEKIT_URL` | ✅ | Your LiveKit Cloud WSS URL |
| `LIVEKIT_API_KEY` | ✅ | LiveKit API key |
| `LIVEKIT_API_SECRET` | ✅ | LiveKit API secret |
| `TAVUS_API_KEY` | ✅ | Tavus API key for avatar |
| `TAVUS_REPLICA_ID` | ✅ | Tavus replica (avatar) ID |
| `TAVUS_PERSONA_ID` | ⬜ | Tavus persona ID (optional) |
| `OPENAI_API_KEY` | ✅ | OpenAI key for GPT-4o + summaries |
| `DEEPGRAM_API_KEY` | ✅ | Deepgram key for STT |
| `DB_PATH` | ⬜ | SQLite DB path (default: `voice_agent.db`) |
| `ALLOWED_ORIGIN` | ⬜ | CORS origin for production (default: `*`) |

---

## 🧪 Running Tests

```bash
pytest backend/tests/ -v
```

---

## 🌐 Production Deployment

See [**Deployment Guide**](./DEPLOYMENT.md) for full step-by-step instructions.

**Quick overview:**
| Component | Platform | Notes |
|---|---|---|
| Frontend | [Vercel](https://vercel.com) | Set `VITE_TOKEN_SERVER_URL` env var |
| Token Server | [Render](https://render.com) Web Service | `python -m backend.token_server` |
| Agent Worker | [Render](https://render.com) Background Worker | `python -m backend.main start` |
| Database | Render Disk (1 GB, ~$1/mo) | Mount at `/data`, set `DB_PATH=/data/voice_agent.db` |

---

## 🛡️ Security Notes

- **Never commit `.env`** — it is listed in `.gitignore`
- In production, set `ALLOWED_ORIGIN` to your exact frontend domain (not `*`)
- Rate-limit the `/token` endpoint to prevent API billing abuse
- Set LiveKit token TTL to 900s (15 min) for short-lived sessions
- See `ARCHITECTURE.md` for the full security threat model

---

## 🗺️ Roadmap

- [ ] OTP (SMS) verification before joining a call
- [ ] PostgreSQL migration for production-grade persistence
- [ ] Multi-language support (Hindi, Tamil, etc.)
- [ ] Doctor availability management dashboard
- [ ] Email/SMS appointment reminders

---

## 📄 License

MIT © 2026 CareVoice AI
