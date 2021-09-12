import os
import urllib.request

from collections import defaultdict

TMP = os.getenv("TMP", "/tmp")
DATA = "safari.logs"
SAFARI_LOGS = os.path.join(TMP, DATA)
PY_BOOK, OTHER_BOOK = "🐍", "."

urllib.request.urlretrieve(
    f"https://bites-data.s3.us-east-2.amazonaws.com/{DATA}", SAFARI_LOGS
)


def create_chart():

    log_days = defaultdict(list)

    with open(SAFARI_LOGS, "r") as safari_logs:
        log_lines = safari_logs.readlines()

        for idx, log_line in enumerate(log_lines, 0):
            if "sending to slack channel" in log_line:
                log_day, _ = log_line.split(" ", 1)
                if "python" in log_lines[idx - 1].lower():
                    log_days[log_day].append(PY_BOOK)
                else:
                    log_days[log_day].append(OTHER_BOOK)

    histogram = list(log_days.items())
    histogram.sort()
    for k, v in histogram:
        vals = "".join(v)
        print(f"{k} {vals}")


create_chart()
