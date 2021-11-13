from datetime import date


from dateutil.rrule import rrule, DAILY


def get_mothers_day_date(year):
    """Given the passed in year int, return the date Mother's Day
    is celebrated assuming it's the 2nd Sunday of May."""
    may_first = date(year=year, month=5, day=1)

    dt_gen = rrule(freq=DAILY, dtstart=may_first, count=31)
    sundays = [d for d in dt_gen if d.date().weekday() == 6]
    return sundays[1].date()


if __name__ == "__main__":
    print(get_mothers_day_date(2020))
