from datetime import datetime, timedelta, date

import re

TODAY = date(2018, 11, 12)


DATE_RGX = re.compile(r"(\d{4})-(\d{2})-(\d{2})")

DATA = """
    +------------+------------+---------+
    | date       | activity   | count   |
    |------------+------------+---------|
    | 2018-11-11 | pcc        | 1       |
    | 2018-11-09 | 100d       | 1       |
    | 2018-11-07 | 100d       | 2       |
    | 2018-10-23 | pcc        | 1       |
    | 2018-10-15 | pcc        | 1       |
    | 2018-10-05 | bite       | 1       |
    | 2018-09-21 | bite       | 4       |
    | 2018-09-18 | bite       | 2       |
    | 2018-09-18 | bite       | 4       |
    +------------+------------+---------+
"""


def extract_dates(data):
    """Extract unique dates from DB table representation as shown in Bite"""

    dates = []
    for line in data.splitlines():
        matches = DATE_RGX.findall(line)
        if not matches:
            continue
        dates.append(date(*[int(s) for s in matches[0]]))
    return sorted(set(dates), reverse=True)


def calculate_streak(dates):
    """Receives sequence (set) of dates and returns number of days
    on coding streak.

    Note that a coding streak is defined as consecutive days coded
    since yesterday, because today is not over yet, however if today
    was coded, it counts too of course.

    So as today is 12th of Nov, having dates 11th/10th/9th of Nov in
    the table makes for a 3 days coding streak.

    See the tests for more examples that will be used to pass your code.
    """

    dates = [TODAY] + dates
    deltas = [(today - yesterday).days for today, yesterday in zip(dates, dates[1:])]

    streak = 0

    print(deltas)
    for delta in deltas:
        if delta > 1:
            break
        streak += 1
    return streak


if __name__ == "__main__":
    dates = extract_dates(DATA)
    print(len(dates))
    print(dates)
    print(calculate_streak(dates))
