"""
voice.py
Handles text-to-speech output for FRIDAY.
"""

from __future__ import annotations

import pyttsx3


_engine = pyttsx3.init()


def _set_voice_preferences() -> None:
    """
    Try to set a female-sounding voice if available.
    Falls back to default voice if no suitable option is found.
    """
    try:
        voices = _engine.getProperty("voices")
        preferred_keywords = ("female", "zira", "hazel", "susan", "samantha")

        for voice in voices:
            descriptor = f"{voice.name} {voice.id}".lower()
            if any(keyword in descriptor for keyword in preferred_keywords):
                _engine.setProperty("voice", voice.id)
                break
    except Exception:
        # Keep default voice if any lookup fails.
        pass

    _engine.setProperty("rate", 180)
    _engine.setProperty("volume", 1.0)


_set_voice_preferences()


def speak(text: str) -> None:
    """
    Speak and log FRIDAY response.
    """
    print(f"FRIDAY: {text}")
    _engine.say(text)
    _engine.runAndWait()
