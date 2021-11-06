from collections import namedtuple
from datetime import datetime

TimeOffset = namedtuple("TimeOffset", "offset date_str divider")

NOW = datetime.now()
MINUTE, HOUR, DAY = 60, 60 * 60, 24 * 60 * 60
TIME_OFFSETS = (
    TimeOffset(10, "just now", None),
    TimeOffset(MINUTE, "{} seconds ago", None),
    TimeOffset(2 * MINUTE, "a minute ago", None),
    TimeOffset(HOUR, "{} minutes ago", MINUTE),
    TimeOffset(2 * HOUR, "an hour ago", None),
    TimeOffset(DAY, "{} hours ago", HOUR),
    TimeOffset(2 * DAY, "yesterday", None),
)


def pretty_date(date):
    """Receives a datetime object and converts/returns a readable string
    using TIME_OFFSETS"""

    if not isinstance(date, datetime) or date > NOW:
        raise ValueError()

    for offset, date_str, divider in TIME_OFFSETS:
        delta = NOW - date
        if delta.total_seconds() < offset:
            if not divider:
                return date_str.format(int(delta.total_seconds()))
            else:
                return date_str.format(int(delta.total_seconds() / divider))
            break
    return date.strftime("%m/%d/%y")
