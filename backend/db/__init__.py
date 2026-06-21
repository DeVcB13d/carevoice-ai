"""Database initialization and connection management."""

import sqlite3
import os
from pathlib import Path
from typing import Optional


class Database:
    """SQLite database manager."""

    def __init__(self, db_path: str = "voice_agent.db"):
        """Initialize database connection."""
        self.db_path = db_path
        self._ensure_db_exists()
        self.seed_dynamic_slots()

    def _ensure_db_exists(self):
        """Create database and schema if it doesn't exist."""
        # Create database file if missing
        if not os.path.exists(self.db_path):
            Path(self.db_path).touch()

        # Load and execute schema
        schema_path = Path(__file__).parent / "schema.sql"
        if schema_path.exists():
            with open(schema_path, "r") as f:
                schema = f.read()

            conn = sqlite3.connect(self.db_path)
            try:
                conn.executescript(schema)
                conn.commit()
            finally:
                conn.close()

    def seed_dynamic_slots(self):
        """Seed available slots for today and the next 7 days for all doctors."""
        from datetime import datetime, timedelta
        conn = self.get_connection()
        try:
            cursor = conn.cursor()
            # Fetch all doctors
            cursor.execute("SELECT id FROM doctors")
            doctors = [row[0] for row in cursor.fetchall()]
            if not doctors:
                # Fallback if doctors table is empty
                doctors = [1, 2, 3]

            today = datetime.now().date()
            times = ['09:00', '10:00', '11:00', '14:00', '15:00', '16:00']
            for i in range(8):  # today + 7 days
                date_str = (today + timedelta(days=i)).strftime('%Y-%m-%d')
                for doc_id in doctors:
                    for t in times:
                        cursor.execute(
                            "INSERT OR IGNORE INTO time_slots (date, time, available, doctor_id) VALUES (?, ?, 1, ?)",
                            (date_str, t, doc_id)
                        )
            conn.commit()
        finally:
            conn.close()

    def get_connection(self) -> sqlite3.Connection:
        """Get a database connection."""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def execute(self, query: str, params: tuple = None) -> Optional[sqlite3.Cursor]:
        """Execute a query."""
        conn = self.get_connection()
        try:
            cursor = conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            conn.commit()
            return cursor
        finally:
            conn.close()

    def fetchall(self, query: str, params: tuple = None) -> list:
        """Fetch all results."""
        conn = self.get_connection()
        try:
            cursor = conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            return cursor.fetchall()
        finally:
            conn.close()

    def fetchone(self, query: str, params: tuple = None) -> Optional[sqlite3.Row]:
        """Fetch single result."""
        conn = self.get_connection()
        try:
            cursor = conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            return cursor.fetchone()
        finally:
            conn.close()

    def close(self):
        """Close all connections."""
        pass  # SQLite handles this automatically


# Global database instance
_db_instance: Optional[Database] = None


def get_db() -> Database:
    """Get or create the global database instance."""
    global _db_instance
    if _db_instance is None:
        _db_instance = Database()
    return _db_instance
