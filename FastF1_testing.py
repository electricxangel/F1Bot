import fastf1.plotting
from datetime import date, datetime
import pandas as pd
from matplotlib import pyplot as plt

fastf1.plotting.setup_mpl(mpl_timedelta_support=False, misc_mpl_mods=False, color_scheme="fastf1")


race_info = []

def get_event_schedule(year):
    schedule = fastf1.get_event_schedule(year=year)
    for i in range(1, 25):
        event = schedule.get_event_by_round(i)
        print(f"{event.EventDate}: {event.Location}, {event.Country}")


def get_most_recent():
    current_date = datetime.now()
    most_recent = datetime.now()

    for i in range(1, 25):
        schedule = fastf1.get_event_schedule(year=current_date.year)
        event = schedule.get_event_by_round(i)
        date = event.EventDate
        if date.to_pydatetime() < current_date:
            most_recent = event
        else:
            print(f"{most_recent.EventDate}: {most_recent.Location}, {most_recent.Country}")
            return most_recent

            break

def plot_graph(race):
    session = fastf1.get_session(race.EventDate.year, race.Location, "R")
    session.load(telemetry=False, weather=False)
    
    fig, ax = plt.subplots(figsize=(8.0, 4.9))

    for drv in session.drivers:
        drv_laps = session.laps.pick_driver(drv)

        abb = drv_laps["Driver"].iloc[0]
        style = fastf1.plotting.get_driver_style(identifier=abb,
                                                 style=["color", "linestyle"],
                                                 session=session)
        ax.plot(drv_laps["LapNumber"], drv_laps["Position"],
                label=abb, **style)

    ax.set_ylim([20.5, 0.5])
    ax.set_yticks([1, 5, 10, 15, 20])
    ax.set_xlabel('Lap')
    ax.set_ylabel('Position')

    ax.legend(bbox_to_anchor=(1.0, 1.02))
    plt.tight_layout()

    plt.savefig(f"graphs/{race.EventDate.year}, {race.Location}")
    plt.show()


def single_driver_graph(driver):
    max = get_most_recent

    for i in range(1, 25):






get_event_schedule(2025)
print("-------------------------------------------------------")
most_recent_race = get_most_recent()
plot_graph(most_recent_race)