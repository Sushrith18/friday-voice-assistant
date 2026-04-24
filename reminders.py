"""
reminders.py
Stores and retrieves reminders from local JSON.
"""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
REMINDERS_FILE = DATA_DIR / "reminders.json"


def _ensure_reminders_file() -> None:
    """
    Create data directory and reminders file if missing.
    """
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    if not REMINDERS_FILE.exists():
        REMINDERS_FILE.write_text("[]", encoding="utf-8")


def _read_raw() -> list[dict]:
    _ensure_reminders_file()
    try:
        content = REMINDERS_FILE.read_text(encoding="utf-8").strip()
        if not content:
            return []
        data = json.loads(content)
        return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        # Return empty list if file is corrupted/unreadable.
        return []


def _write_raw(reminders: list[dict]) -> bool:
    _ensure_reminders_file()
    try:
        REMINDERS_FILE.write_text(
            json.dumps(reminders, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
        return True
    except OSError:
        return False


def add_reminder(text: str) -> bool:
    """
    Add reminder text with timestamp.
    """
    clean_text = text.strip()
    if not clean_text:
        return False

    reminders = _read_raw()
    reminders.append(
        {
            "text": clean_text,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
    )
    return _write_raw(reminders)


def get_reminders() -> list[dict]:
    """
    Return all reminders as a list of dictionaries.
    """
    return _read_raw()
