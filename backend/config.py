"""Configuration loading from environment variables."""

import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Application configuration."""

    # LiveKit
    LIVEKIT_URL = os.getenv("LIVEKIT_URL", "wss://voicerhealth-77yely9v.livekit.cloud")
    LIVEKIT_API_KEY = os.getenv("LIVEKIT_API_KEY", "")
    LIVEKIT_API_SECRET = os.getenv("LIVEKIT_API_SECRET", "")

    # STT (Speech-to-Text)
    DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY", "")

    # TTS (Text-to-Speech)
    CARTESIA_API_KEY = os.getenv("CARTESIA_API_KEY", "")

    # LLM
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    LLM_MODEL = os.getenv("LLM_MODEL", "gpt-4o-mini")

    # Avatar (optional)
    TAVUS_REPLICA_ID = os.getenv("TAVUS_REPLICA_ID", "")
    TAVUS_API_KEY = os.getenv("TAVUS_API_KEY", "")
    TAVUS_PERSONA_ID = os.getenv("TAVUS_PERSONA_ID", "")

    # Database
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///voice_agent.db")

    # Agent settings
    AGENT_NAME = "HealthcareAssistant"
    VOICE_TIMEOUT = 30.0
    SPEECH_TIMEOUT = 3.0

    @classmethod
    def validate(cls):
        """Validate required config is present."""
        required = [
            "LIVEKIT_URL",
            "LIVEKIT_API_KEY",
            "LIVEKIT_API_SECRET",
            "DEEPGRAM_API_KEY",
            "CARTESIA_API_KEY",
            "OPENAI_API_KEY",
        ]
        missing = [key for key in required if not getattr(cls, key)]
        if missing:
            raise ValueError(f"Missing required config: {', '.join(missing)}")
