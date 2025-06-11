import fastf1.plotting
from datetime import date, datetime
import pandas as pd

fastf1.plotting.setup_mpl(mpl_timedelta_support=False, misc_mpl_mods=False, color_scheme="fastf1")


race_info = []

def event_schedule(year):
    schedule = fastf1.get_event_schedule(year=year)
    for i in range(1, 24):
        event = schedule.get_event_by_round(i)
        print(f"{event.EventDate}: {event.Location}, {event.Country}")


def get_most_recent():
    current_date = datetime.now()
    most_recent = datetime.now()

    for i in range(1, 24):
        schedule = fastf1.get_event_schedule(year=current_date.year)
        event = schedule.get_event_by_round(i)
        date = event.EventDate
        if date.to_pydatetime() < current_date:
            most_recent = event
        else:
            print(f"{most_recent.EventDate}: {most_recent.Location}, {most_recent.Country}")
            break




get_most_recent()