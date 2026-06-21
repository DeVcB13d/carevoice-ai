# Voice AI Agent - Architecture

## System Overview

```
┌──────────────────────────────────────────────────────────────┐
│                    FRONTEND (Phase 5)                        │
│  Vite/React → Call Button → Transcript → Avatar Display    │
└────────────────────┬─────────────────────────────────────────┘
                     │ WebSocket (LiveKit)
                     ▼
┌──────────────────────────────────────────────────────────────┐
│              LIVEKIT CLOUD (Voice Transport)                 │
│  wss://voicerhealth-77yely9v.livekit.cloud                 │
│  - Room management                                           │
│  - Media streaming                                           │
│  - WebRTC handling                                           │
└────────────────────┬─────────────────────────────────────────┘
                     │ Agent Service Protocol
                     ▼
┌──────────────────────────────────────────────────────────────┐
│         PYTHON BACKEND (This Implementation)                 │
│                                                              │
│  main.py                                                    │
│  └─ HealthcareAgent (agent/conversation.py)                │
│     ├─ STT Pipeline (Deepgram)                             │
│     │  └─ Audio → Text                                      │
│     ├─ LLM Processing (OpenAI)                             │
│     │  └─ Text → Intent → Tool Calls                       │
│     ├─ Tool Handlers                                        │
│     │  ├─ identify_user                                     │
│     │  ├─ fetch_slots                                       │
│     │  ├─ book_appointment                                  │
│     │  ├─ retrieve_appointments                             │
│     │  ├─ cancel_appointment                                │
│     │  ├─ modify_appointment                                │
│     │  └─ end_conversation                                  │
│     ├─ TTS Pipeline (Cartesia)                             │
│     │  └─ Text → Audio                                      │
│     └─ State Management (ConversationState)                │
│        └─ Track call_id, user_id, extracted info           │
│                                                              │
│  config.py                                                  │
│  └─ API credentials & settings                             │
│                                                              │
│  db.py                                                      │
│  └─ SQLite connection & queries                            │
│                                                              │
└────────────────────┬─────────────────────────────────────────┘
                     │ SQL Queries
                     ▼
┌──────────────────────────────────────────────────────────────┐
│           DATABASE (SQLite: voice_agent.db)                  │
│                                                              │
│  users                  → user profiles                     │
│  time_slots             → available appointment times       │
│  appointments           → booked appointments               │
│  conversation_history   → call transcripts                  │
│  call_summaries         → generated summaries               │
│                                                              │
└──────────────────────────────────────────────────────────────┘

EXTERNAL APIs (Right side)
├─ Deepgram (STT): a303de57915248263ccd3c44fa322abf9bfd4b5c
├─ Cartesia (TTS): sk_car_y1iKhvegJJcSfHEkpGWatY
├─ OpenAI (LLM): sk-proj-K_BUn--kYVIqx0nOyZM2rx3vJIx...
├─ LiveKit (Voice): wss://voicerhealth-77yely9v.livekit.cloud
└─ Tavus (Avatar): 3b269a22f07449818d70cb95d175a458 (optional)
```

---

## Module Dependency Graph

```
main.py
│
└─ config.py
   └─ Load .env
│
└─ agent/conversation.py (HealthcareAgent)
   ├─ config.py (get API keys)
   ├─ agent/prompts.py (SYSTEM_PROMPT, TOOL_DEFINITIONS)
   ├─ db.py (database operations)
   │  └─ sqlite3
   ├─ livekit.agents (voice framework)
   ├─ livekit.agents.deepgram (STT)
   ├─ livekit.agents.cartesia (TTS)
   └─ livekit.agents.openai (LLM)
```

**No circular dependencies** ✅
**Single responsibility per module** ✅
**Easy to test in isolation** ✅

---

## Data Flow: Full Conversation Example

### 1. User Speaks
```
User Audio
  ↓
LiveKit (captures voice)
  ↓
Backend (receives audio stream)
```

### 2. STT: Convert Speech → Text
```
User: "Hi, I'm John Smith, 5551234567"
  ↓
Deepgram STT (processes audio)
  ↓
Text: "Hi, I'm John Smith, 5551234567"
```

### 3. LLM: Understand Intent & Route to Tools
```
System Prompt: "You are a healthcare assistant..."
Context: Previous messages (if any)
Current: "Hi, I'm John Smith, 5551234567"
  ↓
OpenAI LLM (understands intent: identify user)
  ↓
Tool Call: identify_user(name="John Smith", phone="5551234567")
```

### 4. Tool Handler: Execute Business Logic
```
_identify_user(name="John Smith", phone="5551234567")
  ↓
Query: SELECT id FROM users WHERE phone = '5551234567'
  ↓
Not found → INSERT INTO users
  ↓
Save to state: state.user_id = 1, state.user_name = "John Smith"
  ↓
Return: "User identified: John Smith (ID: 1)"
```

### 5. LLM: Generate Response
```
System sees tool result
  ↓
Generates response: "Great John! When would you like to book?"
```

### 6. TTS: Convert Text → Speech
```
Text: "Great John! When would you like to book?"
  ↓
Cartesia TTS (synthesizes voice)
  ↓
Audio stream (with phoneme timing for lip-sync)
  ↓
Sent to user speaker
```

### 7. Storage: Log Everything
```
Conversation History:
- [user] "Hi, I'm John Smith, 5551234567"
- [assistant] "Great John! When would you like to book?"

State:
- call_id: "abc-123-def"
- user_id: 1
- user_name: "John Smith"
- message_count: 2
```

---

## Tool Handler Architecture

Each tool follows this pattern:

```python
def _tool_name(self, args: dict) -> ChatMessage:
    """
    1. Extract arguments
    2. Validate (if needed)
    3. Query/modify database
    4. Update conversation state
    5. Return result as ChatMessage
    """
    
    param = args.get("key")
    
    # Database operation
    db = get_db()
    result = db.fetchone("SELECT ...", (param,))
    
    if success:
        # Update state
        self.state.field = value
        return ChatMessage(role="tool", content="Success message")
    else:
        return ChatMessage(role="tool", content="Error message")
```

### Example: book_appointment

```python
def _book_appointment(self, args: dict) -> ChatMessage:
    user_id = args.get("user_id")
    slot_id = args.get("slot_id")
    
    db = get_db()
    
    # 1. Check slot is available (prevent double-booking)
    slot = db.fetchone("SELECT available FROM time_slots WHERE id = ?", (slot_id,))
    if not slot["available"]:
        return ChatMessage(role="tool", content="Slot already booked")
    
    # 2. Create appointment
    cursor = db.execute(
        "INSERT INTO appointments (user_id, slot_id) VALUES (?, ?)",
        (user_id, slot_id)
    )
    appointment_id = cursor.lastrowid
    
    # 3. Mark slot unavailable
    db.execute("UPDATE time_slots SET available = 0 WHERE id = ?", (slot_id,))
    
    # 4. Update state
    self.state.booked_slot_id = slot_id
    
    # 5. Return success
    return ChatMessage(role="tool", content=f"Appointment {appointment_id} booked!")
```

---

## State Management (ConversationState)

Tracks information throughout the call:

```python
@dataclass
class ConversationState:
    call_id: str              # Unique ID for this call
    user_id: Optional[int]    # Database user ID
    user_name: Optional[str]  # Patient name
    user_phone: Optional[str] # Patient phone
    extracted_date: Optional[str]  # Selected date (YYYY-MM-DD)
    extracted_time: Optional[str]  # Selected time
    booked_slot_id: Optional[int]  # Confirmed appointment slot
    message_count: int        # Total back-and-forth exchanges
    started_at: datetime      # Call start timestamp
```

**Why separate from LLM context?**
- LLM has 5-10 message window for speed
- State persists the important facts
- Easy to extract for summary

---

## Latency Budget

Target: **<3-5 seconds per response**

```
User speaks (2-3s)
  ↓
Deepgram STT: 500-1000ms
  ↓
LLM inference: 500-1000ms
  ↓
Database query: 10-50ms
  ↓
Cartesia TTS: 300-800ms (streamed, doesn't block)
  ↓
Network/codec overhead: 200-400ms
  ────────────────────────────
  Total: 1500-3250ms ✅ Under 5s
```

---

## Database Operations

### User Identification
```sql
SELECT id FROM users WHERE phone = ?
-- vs --
INSERT INTO users (name, phone) VALUES (?, ?)
```

### Slot Selection
```sql
SELECT id, time FROM time_slots 
WHERE date = ? AND available = 1 
ORDER BY time
-- Indexed on (date, available) for speed
```

### Appointment Booking (Atomic)
```sql
BEGIN TRANSACTION
  INSERT INTO appointments (...) -- Gets ID
  UPDATE time_slots SET available = 0 WHERE id = ?
COMMIT
-- Prevents double-booking
```

---

## Configuration & Secrets

All API keys in `.env` → loaded by `config.py`:

```python
class Config:
    LIVEKIT_URL = os.getenv("LIVEKIT_URL")
    DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")
    CARTESIA_API_KEY = os.getenv("CARTESIA_API_KEY")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    # ... etc
    
    @classmethod
    def validate(cls):
        # Check all required keys present
        if not cls.DEEPGRAM_API_KEY:
            raise ValueError("Missing DEEPGRAM_API_KEY")
```

**Never commit `.env`** → Use `.gitignore`

---

## Error Handling Strategy

### Level 1: Config Validation
```python
Config.validate()  # Fails immediately if missing keys
```

### Level 2: Database Operations
```python
try:
    cursor = db.execute(...)
except Exception as e:
    return ChatMessage(role="tool", content=f"Error: {str(e)}")
```

### Level 3: Tool Handlers
```python
async def _execute_tool(self, tool_call):
    try:
        return self._identify_user(args)
    except Exception as e:
        logger.error(f"Tool error: {e}")
        return error_message
```

### Level 4: Main Loop
```python
try:
    await agent.run()
except Exception as e:
    logger.error(f"Agent crashed: {e}")
    # Graceful shutdown
```

---

## Scalability Considerations (Future)

### Phase 1-3 (MVP): SQLite
- ✅ Good for single deployment
- ✅ Zero DevOps overhead
- ✅ Sufficient for 48-hour demo

### Phase 4+ (Scale): PostgreSQL
```python
# Just change config
DATABASE_URL = "postgresql://user:pass@host/db"
```

### Concurrency
- SQLite: ~1-2 concurrent calls
- PostgreSQL: Unlimited (with connection pooling)
- Redis: Add for session caching

### Monitoring
- Add logging to tool handlers
- Track latency per stage
- Monitor database query performance

---

## Testing Strategy

### Unit Tests (Phase 2)
```python
# test_tools.py
def test_identify_user():
    agent = HealthcareAgent()
    result = agent._identify_user({"name": "John", "phone": "555"})
    assert "identified" in result.content

def test_double_booking():
    agent = HealthcareAgent()
    # Book same slot twice, second should fail
    result1 = agent._book_appointment({"user_id": 1, "slot_id": 1})
    result2 = agent._book_appointment({"user_id": 2, "slot_id": 1})
    assert "already booked" in result2.content
```

### Integration Tests
```python
# Full conversation flow
async def test_full_conversation():
    # User: "I'm John, 555"
    # Agent calls: identify_user()
    # User: "Next Tuesday at 2pm"
    # Agent calls: fetch_slots() → book_appointment()
    # Verify: appointment in database
```

---

## Summary

**Modular, testable, production-ready architecture.**

- 🎯 Single responsibility per module
- 🔄 Clean data flow through layers
- 🛡️ Error handling at each level
- ⚡ Latency-optimized
- 🔒 Secure credential management
- 📊 State tracking throughout
- 🗄️ Database-backed persistence

Ready for Phase 1: Voice I/O Testing! 🚀
