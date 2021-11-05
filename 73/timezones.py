import pytz
from datetime import datetime

MEETING_HOURS = range(6, 23)  # meet from 6 - 22 max
TIMEZONES = set(pytz.all_timezones)


def within_schedule(utc, *timezones):
    """Receive a utc datetime and one or more timezones and check if
    they are all within schedule (MEETING_HOURS)"""
    try:
        return all(
            (
                pytz.utc.localize(utc).astimezone(pytz.timezone(tz)).hour
                in MEETING_HOURS
                for tz in timezones
            )
        )
    except pytz.exceptions.UnknownTimeZoneError as e:
        raise ValueError()


if __name__ == "__main__":
    print(within_schedule(datetime(2018, 4, 18, 12, 28), *["Europe/Madrid"]))
    print(within_schedule(datetime(2018, 4, 18, 12, 28), *["Europe/Madrid", "bogus"]))
