# Voice AI Agent - Backend

## Project Structure

```
backend/
├── main.py                 # Entry point - starts the agent worker
├── config.py              # Configuration from environment variables
├── db.py                  # Database connection and utilities
│
├── agent/                 # Agent logic and conversation management
│   ├── __init__.py
│   ├── conversation.py    # Main agent class with tool handlers
│   └── prompts.py         # System prompts and tool definitions
│
├── tools/                 # Tool implementations (for Phase 2+)
│   └── __init__.py
│
├── models/                # Data models (for Phase 2+)
│   └── __init__.py
│
├── db/                    # Database schema and migrations
│   ├── __init__.py
│   └── schema.sql         # SQLite schema with sample data
│
└── README.md              # This file
```

## Module Breakdown

### `main.py`
**Purpose:** Entry point for the application
- Starts the LiveKit worker
- Initializes the healthcare agent
- Handles job context and lifecycle

**When to modify:**
- Add logging/monitoring
- Add error handling for worker crashes
- Add health check endpoints

### `config.py`
**Purpose:** Centralized configuration management
- Loads all environment variables from `.env`
- Provides validation of required credentials
- Centralized place for constants

**When to modify:**
- Add new configuration options
- Change default values
- Add environment-specific configs

### `db.py`
**Purpose:** Database abstraction layer
- SQLite connection management
- Query execution wrapper
- Global database instance

**When to modify:**
- Add connection pooling for higher concurrency
- Migrate to PostgreSQL
- Add transaction management

### `agent/conversation.py`
**Purpose:** Core agent logic
- `HealthcareAgent` class - main agent
- `ConversationState` - tracks session state
- Tool implementations (identify_user, fetch_slots, etc.)
- Message handling and routing

**When to modify:**
- Add new tools
- Change conversation logic
- Modify tool behavior

### `agent/prompts.py`
**Purpose:** System prompts and tool schemas
- `SYSTEM_PROMPT` - agent behavior and instructions
- `TOOL_DEFINITIONS` - OpenAI tool schema
- `SUMMARY_PROMPT` - summary generation instructions

**When to modify:**
- Tune agent personality
- Change tool descriptions
- Modify prompt structure

### `db/schema.sql`
**Purpose:** Database schema and initial data
- Table definitions
- Indexes for performance
- Sample appointment slots

**When to modify:**
- Add new tables
- Change column definitions
- Add more sample data

## Running the Agent

### Development (Local Testing)

```bash
# From project root
python -m backend.main
```

This starts a local agent that can be connected via LiveKit frontend.

### With LiveKit CLI

```bash
# Run with LiveKit development tools
livekit-cli rooms create test-room
python -m backend.main
```

### Docker

```bash
docker build -f backend.Dockerfile -t voice-agent .
docker run --env-file .env voice-agent
```

## Database Schema

### Tables

**users**
- `id` (PK)
- `name` - Patient name
- `phone` - Unique phone identifier
- `email` - Optional email
- `created_at`, `updated_at`

**time_slots**
- `id` (PK)
- `date` - Appointment date
- `time` - Time slot
- `available` - Whether slot is available
- `booked_at` - When it was booked
- Indexed on (date, available) for fast lookups

**appointments**
- `id` (PK)
- `user_id` (FK)
- `slot_id` (FK) - Unique to prevent double-booking
- `status` - 'booked', 'cancelled', 'completed'
- `notes`
- `created_at`, `cancelled_at`

**conversation_history**
- `id` (PK)
- `call_id` - Links to a specific call session
- `role` - 'user' or 'assistant'
- `content` - Message text
- `created_at`
- Indexed on (call_id, created_at)

**call_summaries**
- `id` (PK)
- `call_id` (unique)
- `appointment_id` (FK)
- `summary` - Generated summary
- `generated_at`

## Tool Handler Flow

When LLM calls a tool:

```
LLM → Tool Call (JSON)
  ↓
_execute_tool() routes to handler
  ↓
Handler modifies database
  ↓
Handler returns result as ChatMessage
  ↓
LLM receives result and continues
```

### Available Tools

1. **identify_user** - Create/get user from phone
2. **fetch_slots** - Show available times for a date
3. **book_appointment** - Create appointment, lock slot
4. **retrieve_appointments** - Show user's bookings
5. **cancel_appointment** - Mark as cancelled, free slot
6. **modify_appointment** - Reschedule to new slot
7. **end_conversation** - Generate summary

## Development Workflow

### Phase 1: Voice I/O (Current)
- ✅ Config loading
- ✅ Database initialization
- ✅ Agent skeleton
- ⏳ Test voice loop (next)

### Phase 2: Tools & Database
- Implement tool handlers (already done as stubs)
- Test each tool independently
- Test double-booking prevention
- Test appointment lifecycle

### Phase 3: Context Management
- Enhance conversation state tracking
- Implement context window management
- Add conversation summarization

### Phase 4-7
- Frontend
- Summary generation
- Deployment
- Polish

## Testing

### Unit Tests (Not yet written)

```bash
pytest backend/tests/test_tools.py
pytest backend/tests/test_conversation.py
```

### Manual Testing

```bash
# Start agent
python -m backend.main

# In another terminal, test tool calls
python -c "
from backend.db import get_db
db = get_db()
users = db.fetchall('SELECT * FROM users')
print(f'Users: {len(users)}')
"
```

## Common Issues

### Error: "No module named 'backend'"
Make sure you're running from project root: `python -m backend.main`

### Error: "DEEPGRAM_API_KEY not set"
Check `.env` file exists in project root with all credentials.

### Database locked
This can happen with concurrent writes. Use proper transaction handling.

### Tool call not executing
Check the tool name matches exactly. LLM is case-sensitive.

## Next Steps

1. Install dependencies: `pip install -r requirements.txt`
2. Test database: `python -c "from backend.db import get_db; get_db()"`
3. Start agent: `python -m backend.main`
4. Connect frontend and test voice loop
