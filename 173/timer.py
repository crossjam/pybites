from datetime import datetime, timedelta
import re

NOW = datetime(year=2019, month=2, day=6, hour=22, minute=0, second=0)

TIME_UNIT_RGX = re.compile(r"(\d+)([hmds])?")


def add_todo(delay_time: str, task: str, start_time: datetime = NOW) -> str:
    """
    Add a todo list item in the future with a delay time.

    Parse out the time unit from the passed in delay_time str:
    - 30d = 30 days
    - 1h 10m = 1 hour and 10 min
    - 5m 3s = 5 min and 3 seconds
    - 45 or 45s = 45 seconds

    Return the task and planned time which is calculated from
    provided start_time (here default = NOW):
    >>> add_todo("1h 10m", "Wash my car")
    >>> "Wash my car @ 2019-02-06 23:10:00"
    """

    arg_map = {"s": "seconds", "": "seconds", "m": "minutes", "h": "hours", "d": "days"}
    dt_args = {"days": 0, "hours": 0, "minutes": 0, "seconds": 0}

    matches = TIME_UNIT_RGX.findall(delay_time)
    for magnitude, time_spec in matches:
        magnitude = int(magnitude)
        dt_args[arg_map[time_spec]] = magnitude

    td = timedelta(**dt_args)
    deadline = (start_time + td).strftime("%Y-%m-%d %H:%M:%S")
    return f"{task} @ {deadline}"


if __name__ == "__main__":
    print(add_todo("1d 10h 47m 17s", "Study some Python"))
