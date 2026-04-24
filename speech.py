"""
speech.py
Handles microphone capture and speech-to-text conversion.
"""

from __future__ import annotations

import speech_recognition as sr


def listen() -> str:
    """
    Capture voice input from microphone and convert it to text.
    Returns lowercase text on success, or empty string on failure.
    """
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=0.7)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)
    except sr.WaitTimeoutError:
        print("User: [no speech detected in time]")
        return ""
    except Exception as err:
        print(f"User: [microphone error: {err}]")
        return ""

    try:
        text = recognizer.recognize_google(audio)
        text = text.strip().lower()
        print(f"User: {text}")
        return text
    except sr.UnknownValueError:
        print("User: [unrecognized speech]")
        return ""
    except sr.RequestError as err:
        print(f"User: [speech service error: {err}]")
        return ""
    except Exception as err:
        print(f"User: [unexpected speech error: {err}]")
        return ""
