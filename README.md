# F1 Calendar Sync to Google Calendar (IST)

This Python script automatically fetches all Formula 1 sessions for the current year's season and adds them to your Google Calendar — all in your selected timezone. Two scripts are available - "script_google_api.py" uploads directly to your Google Calendar & "script_local.py" creates an .ics file in the scripts directory to be dragged and dropped onto Google Calendar. You may use either.

---

## Features

- Fetches official F1 2025 schedule via [FastF1](https://theoehrly.github.io/Fast-F1/)
- Converts session start times to desired timezone
- Adds each session (Practice, Quali, Race, etc.) to your Google Calendar

---

## Setup

### 1. Clone the repo

```bash
git clone https://github.com/ArnavSaikia/f1-google-calendar-updater.git
cd f1-google-calendar-updater
```

### 2. Install dependencies

Make sure you’re using Python 3.9+

```bash
pip install -r requirements.txt
```

### 3. Set up Google Calendar API

- Go to [Google Cloud Console](https://console.cloud.google.com/)
- Create a project and enable the **Google Calendar API**
- Create **OAuth client credentials** (Choose Desktop app and External while creating the credentials)
- Download `credentials.json` and place it in this folder

You’ll be prompted in the browser to sign in and approve access when you first run the script. If you encounter "403 Unverified App Error", go to OAuth consent screen tab and add your desired email under 'Test users'

---

## Running the Script

```bash
python script_google_api.py
```

You’ll see output like:

```
✅ Added: F1 Monaco GP - Qualifying (link to event)
✅ Added: F1 Monaco GP - Race (link to event)
```

---
