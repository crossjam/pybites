from datetime import datetime, date
import re

THIS_YEAR = date.today().year

DATETIME_RGX = re.compile(r".*(\w{3}  ?\d{1,2} \d{2}:\d{2})$")

MAC1 = """
reboot    ~                         Wed Apr 10 22:39
reboot    ~                         Wed Mar 27 16:24
reboot    ~                         Wed Mar 27 15:01
reboot    ~                         Sun Mar  3 14:51
reboot    ~                         Sun Feb 17 11:36
reboot    ~                         Thu Jan 17 21:54
reboot    ~                         Mon Jan 14 09:25
"""


def calc_max_uptime(reboots):
    """Parse the passed in reboots output,
    extracting the datetimes.

    Calculate the highest uptime between reboots =
    highest diff between extracted reboot datetimes.

    Return a tuple of this max uptime in days (int) and the
    date (str) this record was hit.

    For the output above it would be (30, '2019-02-17'),
    but we use different outputs in the tests as well ...
    """

    datetimes = []
    for line in reboots.splitlines():
        matches = DATETIME_RGX.findall(line)
        if not matches:
            continue

        datetimes.append(datetime.strptime(matches[0], "%b %d %H:%M"))

    datetimes = sorted(datetimes)
    deltas = [(d2 - d1, d2) for d1, d2 in zip(datetimes, datetimes[1:])]
    print(deltas)
    max_delta, max_delta_end = max(deltas, key=lambda p: p[0])
    return max_delta.days, max_delta_end.strftime(f"{THIS_YEAR}-%m-%d")


if __name__ == "__main__":
    print(calc_max_uptime(MAC1))
