from ics import Calendar, Event
import fastf1
import pytz
from datetime import datetime, timedelta
import pandas as pd

def main():
    print("Fetching current year data. Do note the program might fail if current year data isn't available from the API yet")
    current_year = datetime.now().year #returns an int

    cal = Calendar()
    schedule = fastf1.get_event_schedule(current_year)
    user_tz_input = input("Enter your timezone (e.g., Asia/Kolkata, Europe/London, America/New_York): ")
    if user_tz_input not in pytz.all_timezones:
        print("Invalid timezone. Defaulting to Asia/Kolkata.")
        user_tz = pytz.timezone("Asia/Kolkata")
    else:
        user_tz = pytz.timezone(user_tz_input)


    for index,row in schedule.iterrows():
        if row['EventFormat'] == 'testing' : continue

        event_name = row['EventName']

        for session in ['Session1','Session2','Session3','Session4','Session5']:
                session_name = row.get(session)
                session_date_utc = row.get(f'{session}DateUtc')
                if pd.notnull(session_date_utc):
                    if session_date_utc.tzinfo is None:
                        session_date_utc = pytz.utc.localize(session_date_utc)
                    session_date_user = session_date_utc.astimezone(user_tz)

                    e = Event()
                    e.name = f'F1 {event_name} - {session_name}'
                    e.begin = session_date_user
                    e.duration = timedelta(hours=2 if session_name == 'Race' else 1)
                    cal.events.add(e)

    safe_tz = user_tz_input.replace("/", "_")
    with open(f'f1_{current_year}_schedule_{safe_tz}.ics','w') as file:
         file.writelines(cal.serialize())

if __name__ == "__main__":
     main()

