from __future__ import print_function
import os.path
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import fastf1
import pandas as pd
from datetime import datetime, timedelta
import pytz

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']

def get_calendar_service():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    else:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return build('calendar', 'v3', credentials=creds)


def add_event(service, summary, start_time, duration):
    end_time = start_time + timedelta(hours = duration)

    event = {
        'summary': summary,
        'start': {
            'dateTime': start_time.isoformat(),
            'timeZone': 'Asia/Kolkata',
        },
        'end': {
            'dateTime': end_time.isoformat(),
            'timeZone': 'Asia/Kolkata',
        },
    }
    created = service.events().insert(calendarId='primary', body=event).execute()
    print(f"✅ Added: {summary} ({created.get('htmlLink')})")


def main():
    service = get_calendar_service()
    
    calendar_list = service.calendarList().list().execute()
    print("✅ Connected to Google Calendar")
    for cal in calendar_list['items']:
        print("📅", cal['summary'])
    
    schedule = fastf1.get_event_schedule(2025)
    ist = pytz.timezone('Asia/Kolkata')


    for index, row in schedule.iterrows():
        if row["EventFormat"]=='testing': continue

        event_name = row['EventName']

        for session in ['Session1','Session2','Session3','Session4','Session5']:
            session_name = row.get(session)
            session_date_utc = row.get(f'{session}DateUtc')
            if pd.notnull(session_date_utc):
                if session_date_utc.tzinfo is None:
                    session_date_utc = pytz.utc.localize(session_date_utc)
                session_date_ist = session_date_utc.astimezone(ist)
                
                title = f'F1 {event_name} - {session_name}'
                add_event(service,title,session_date_ist,1) if session_name!='Race' else add_event(service,title,session_date_ist,2)

if __name__ == '__main__':
    main()
                
