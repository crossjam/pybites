from datetime import date

import dateutil

from dateutil.relativedelta import relativedelta

TODAY = date(year=2018, month=11, day=29)


def get_hundred_weekdays(start_date=TODAY):
    """Return a list of hundred date objects starting from
    start_date up till 100 weekdays later, so +100 days
    skipping Saturdays and Sundays"""

    # one_day = dateutil.relativedelta.relativedelta(days=1)
    one_day = relativedelta(days=1)

    res, cnt = [start_date], 1
    while len(res) < 100:
        next_date, cnt = start_date + (one_day * cnt), cnt + 1
        if next_date.weekday() in (5, 6):
            continue
        res.append(next_date)
    return res


if __name__ == "__main__":
    print(get_hundred_weekdays()[:10])
