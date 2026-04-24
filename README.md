# FRIDAY Voice Assistant

Modular personal voice assistant for Windows, built in Python.

## Features

- Voice input with microphone (`speech_recognition`)
- Text-to-speech output (`pyttsx3`)
- Commands:
  - Open YouTube / Google
  - Open Chrome / VS Code
  - Tell current time and date
  - Add and read reminders
- Reminder persistence in local JSON (`data/reminders.json`)
- Startup greeting based on time of day
- Loop runs continuously until you say `exit`

## Project Structure

- `main.py` - Assistant startup and main runtime loop
- `speech.py` - Voice capture and speech-to-text
- `voice.py` - Text-to-speech output
- `commands.py` - Command parsing and execution logic
- `reminders.py` - Reminder storage and retrieval

## Install and Run (Windows)

1. Create and activate virtual environment:
   - `python -m venv .venv`
   - `.venv\Scripts\activate`

2. Install dependencies:
   - `pip install -r requirements.txt`

3. Run FRIDAY:
   - `python main.py`

## Example Voice Commands

- "open youtube"
- "open google"
- "open chrome"
- "open vs code"
- "what is the time"
- "what is the date"
- "add reminder call mom at 6 pm"
- "show reminders"
- "exit"

## Notes

- FRIDAY always addresses you as "Boss".
- If a female voice is available on your system, FRIDAY tries to use it automatically.
- For microphone recognition, ensure your default input device is set correctly in Windows.
# friday-voice-assistant
Personal AI Voice Assistant (FRIDAY) built with Python
