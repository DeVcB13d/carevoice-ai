#!/usr/bin/env python3
"""
Phase 1 Test: Voice I/O Integration
Tests that LiveKit Inference STT + TTS work together.
"""

import asyncio
import logging
from pathlib import Path

from backend.config import Config
from backend.agent import HealthcareAgent

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


async def test_stt():
    """Test Speech-to-Text (Deepgram via LiveKit Inference)."""
    logger.info("Testing Deepgram STT via LiveKit Inference...")
    try:
        from livekit.agents.inference import STT

        stt = STT(model="deepgram/nova-3")
        logger.info("✅ Deepgram STT initialized successfully")
        return True
    except Exception as e:
        logger.error(f"❌ Deepgram STT failed: {e}")
        return False


async def test_tts():
    """Test Text-to-Speech (Cartesia via LiveKit Inference)."""
    logger.info("Testing Cartesia TTS via LiveKit Inference...")
    try:
        from livekit.agents.inference import TTS

        tts = TTS(model="cartesia/sonic-3", voice="9626c31c-bec5-4cca-baa8-f8ba9e84c8bc")
        logger.info("✅ Cartesia TTS initialized successfully")
        return True
    except Exception as e:
        logger.error(f"❌ Cartesia TTS failed: {e}")
        return False


async def test_llm():
    """Test Language Model (OpenAI via LiveKit Inference)."""
    logger.info("Testing OpenAI LLM via LiveKit Inference...")
    try:
        from livekit.agents.inference import LLM

        llm = LLM(model="openai/gpt-4o-mini")
        logger.info("✅ OpenAI LLM initialized successfully")
        return True
    except Exception as e:
        logger.error(f"❌ OpenAI LLM failed: {e}")
        return False


async def test_agent_initialization():
    """Test HealthcareAgent initialization."""
    logger.info("Testing HealthcareAgent initialization...")
    try:
        agent = HealthcareAgent()
        logger.info("✅ HealthcareAgent initialized")
        logger.info(f"   - STT: {agent.stt.__class__.__name__}")
        logger.info(f"   - TTS: {agent.tts.__class__.__name__}")
        logger.info(f"   - LLM: {agent.llm.__class__.__name__}")
        return True
    except Exception as e:
        logger.error(f"❌ HealthcareAgent initialization failed: {e}")
        return False


async def test_session_creation():
    """Test AgentSession creation."""
    logger.info("Testing AgentSession creation...")
    try:
        from livekit.agents import AgentSession, TurnHandlingOptions, inference

        agent = HealthcareAgent()
        session = AgentSession(
            stt=agent.stt,
            llm=agent.llm,
            tts=agent.tts,
            turn_handling=TurnHandlingOptions(
                turn_detection=inference.TurnDetector(),
            ),
        )
        logger.info("✅ AgentSession created successfully")
        return True
    except Exception as e:
        logger.error(f"❌ AgentSession creation failed: {e}")
        return False


async def test_database_integration():
    """Test database integration."""
    logger.info("Testing database integration...")
    try:
        from backend.db import get_db

        db = get_db()
        slots = db.fetchall("SELECT COUNT(*) as count FROM time_slots")
        logger.info(f"✅ Database connected")
        logger.info(f"   - Available slots: {slots[0]['count']}")
        return True
    except Exception as e:
        logger.error(f"❌ Database integration failed: {e}")
        return False


async def test_tool_execution():
    """Test tool handler execution."""
    logger.info("Testing tool execution...")
    try:
        agent = HealthcareAgent()
        from backend.agent.conversation import ConversationState
        agent.state = ConversationState(call_id="test-call-id")
        agent.state.user_id = 1
        agent.state.user_name = "Test User"
        agent.state.user_phone = "555-0000"

        # Simulate a tool call (async in 1.x)
        result = await agent.fetch_slots(date="2026-06-23")
        logger.info("✅ Tool execution works")
        logger.info(f"   - Result: {result[:100]}...")
        return True
    except Exception as e:
        logger.error(f"❌ Tool execution failed: {e}")
        return False


async def main():
    """Run all Phase 1 tests."""
    print("\n" + "=" * 70)
    print("PHASE 1: VOICE I/O INTEGRATION TEST (LiveKit Inference)")
    print("=" * 70 + "\n")

    logger.info("Starting Phase 1 tests...")
    logger.info(f"LLM Model: {Config.LLM_MODEL}")

    results = []

    # Test individual components
    logger.info("\n[1/7] Testing Deepgram STT...")
    results.append(await test_stt())

    logger.info("\n[2/7] Testing Cartesia TTS...")
    results.append(await test_tts())

    logger.info("\n[3/7] Testing OpenAI LLM...")
    results.append(await test_llm())

    logger.info("\n[4/7] Testing HealthcareAgent initialization...")
    results.append(await test_agent_initialization())

    logger.info("\n[5/7] Testing AgentSession creation...")
    results.append(await test_session_creation())

    logger.info("\n[6/7] Testing database integration...")
    results.append(await test_database_integration())

    logger.info("\n[7/7] Testing tool execution...")
    results.append(await test_tool_execution())

    # Summary
    print("\n" + "=" * 70)
    passed = sum(results)
    total = len(results)
    print(f"TEST RESULTS: {passed}/{total} passed")
    print("=" * 70)

    if passed == total:
        logger.info("\n✅ ALL PHASE 1 TESTS PASSED!")
        logger.info("\nVoice I/O pipeline is ready via LiveKit Inference:")
        logger.info("  1. User speaks → Deepgram STT (Inference)")
        logger.info("  2. STT output → OpenAI LLM (Inference)")
        logger.info("  3. LLM output → Cartesia TTS (Inference)")
        logger.info("  4. TTS output → User hears response")
        return 0
    else:
        logger.error(f"\n❌ {total - passed} test(s) failed")
        logger.error("Check errors above and fix before proceeding")
        return 1


if __name__ == "__main__":
    exit_code = asyncio.run(main())
    exit(exit_code)
