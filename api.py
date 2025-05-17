import fastf1
import pandas as pd
from datetime import datetime
import pytz

# fastf1.Cache.enable_cache('cache')

schedule = fastf1.get_event_schedule(2025)

ist = pytz.timezone('Asia/Kolkata')

for index, row in schedule.iterrows():
    if row["EventFormat"]=='testing': continue

    event_name = row['EventName']

    for session in ['Session1','Session2','Session3','Session4','Session5']:
        session_name = row.get(session)
        session_date_utc = row.get(f'{session}DateUtc')
        if pd.notnull(session_date_utc):
            session_date_ist = session_date_utc.tz_localize('UTC').astimezone(ist)
            print(f"{event_name} - {session_name} starts at {session_date_ist.strftime('%Y-%m-%d %H:%M:%S')} IST")


# print(list(schedule.iterrows()))