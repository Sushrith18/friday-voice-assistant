"""
main.py
Entry point and runtime loop for FRIDAY voice assistant.
"""

from __future__ import annotations

from datetime import datetime

from commands import process_command
from speech import listen
from voice import speak


def _time_based_greeting() -> str:
    hour = datetime.now().hour
    if 5 <= hour < 12:
        return "Good morning Boss"
    if 12 <= hour < 17:
        return "Good afternoon Boss"
    if 17 <= hour < 22:
        return "Good evening Boss"
    return "Hello Boss"


def run_assistant() -> None:
    """
    Main assistant loop.
    """
    speak("FRIDAY online. " + _time_based_greeting())

    while True:
        command = listen()
        if not command:
            speak("Please repeat that Boss.")
            continue

        response, should_exit = process_command(command)
        speak(response)

        if should_exit:
            break


if __name__ == "__main__":
    try:
        run_assistant()
    except KeyboardInterrupt:
        speak("Shutting down. Goodbye Boss")
    except Exception as err:
        # Final catch to prevent abrupt crash in production-like usage.
        print(f"FRIDAY: Unexpected error: {err}")
