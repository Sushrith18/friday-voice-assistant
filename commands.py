"""
commands.py
Command parsing and execution logic for FRIDAY.
"""

from __future__ import annotations

import datetime
import os
import webbrowser

from reminders import add_reminder, get_reminders


def _open_chrome() -> bool:
    """
    Open Google Chrome on Windows.
    """
    try:
        os.startfile("chrome")  # type: ignore[attr-defined]
        return True
    except Exception:
        try:
            os.system("start chrome")
            return True
        except Exception:
            return False


def _open_vscode() -> bool:
    """
    Open Visual Studio Code on Windows.
    """
    try:
        os.startfile("code")  # type: ignore[attr-defined]
        return True
    except Exception:
        try:
            os.system("start code")
            return True
        except Exception:
            return False


def process_command(command: str) -> tuple[str, bool]:
    """
    Process spoken command text.
    Returns (assistant_response, should_exit).
    """
    if not command:
        return "I could not hear you clearly Boss. Please say that again.", False

    text = command.lower().strip()

    if text in {"exit", "quit", "stop", "goodbye"}:
        return "Goodbye Boss", True

    if "open youtube" in text:
        webbrowser.open("https://www.youtube.com")
        return "Yes Boss, opening YouTube", False

    if "open google" in text:
        webbrowser.open("https://www.google.com")
        return "Yes Boss, opening Google", False

    if "open chrome" in text:
        if _open_chrome():
            return "Yes Boss, opening Chrome", False
        return "Sorry Boss, I could not open Chrome.", False

    if "open code" in text or "open visual studio code" in text or "open vs code" in text:
        if _open_vscode():
            return "Yes Boss, opening VS Code", False
        return "Sorry Boss, I could not open VS Code.", False

    if "time" in text:
        now_time = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {now_time} Boss", False

    if "date" in text:
        today = datetime.datetime.now().strftime("%A, %d %B %Y")
        return f"Today's date is {today} Boss", False

    if text.startswith("add reminder"):
        reminder_text = text.replace("add reminder", "", 1).strip(" :,-")
        if not reminder_text:
            return "Please tell me the reminder text Boss.", False

        if add_reminder(reminder_text):
            return f"Reminder added Boss: {reminder_text}", False
        return "Sorry Boss, I could not save that reminder.", False

    if "show reminders" in text or "read reminders" in text or "list reminders" in text:
        reminders = get_reminders()
        if not reminders:
            return "You have no reminders right now Boss.", False

        joined = "; ".join([f"{idx + 1}. {item.get('text', '')}" for idx, item in enumerate(reminders)])
        return f"Here are your reminders Boss: {joined}", False

    return "I am not sure how to handle that yet Boss.", False
