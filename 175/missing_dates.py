from datetime import date

from dateutil.rrule import rrule, DAILY


def get_missing_dates(dates):
    """Receives a range of dates and returns a sequence
    of missing datetime.date objects (no worries about order).

    You can assume that the first and last date of the
    range is always present (assumption made in tests).

    See the Bite description and tests for example outputs.
    """
    start_date, end_date = min(dates), max(dates)
    print((start_date, end_date))

    time_delta = end_date - start_date

    return sorted(
        set(
            (
                d.date()
                for d in rrule(
                    freq=DAILY, count=time_delta.days + 1, dtstart=start_date
                )
            )
        )
        - set(dates)
    )


if __name__ == "__main__":
    print(get_missing_dates([date(year=2019, month=2, day=n) for n in range(1, 11, 2)]))
