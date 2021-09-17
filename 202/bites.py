import csv
import os
import re

from pathlib import Path
from urllib.request import urlretrieve

data = "https://bites-data.s3.us-east-2.amazonaws.com/bite_levels.csv"
tmp = Path(os.getenv("TMP", "/tmp"))
stats = tmp / "bites.csv"

if not stats.exists():
    urlretrieve(data, stats)


def get_most_complex_bites(N=10, stats=stats):
    """Parse the bites.csv file (= stats variable passed in), see example
    output in the Bite description.
    Return a list of Bite IDs (int or str values are fine) of the N
    most complex Bites.
    """

    def extract_bite_id(bite):
        res = re.search(r"Bite (\d+)\.", bite["Bite"])
        return int(res.groups()[0])

    with open(stats, "r", encoding="utf-8-sig") as in_file:
        rdr = csv.DictReader(in_file, delimiter=";")
        rows = [r for r in rdr if r["Difficulty"] != "None"]

    rows.sort(key=lambda row: float(row["Difficulty"]), reverse=True)
    return [extract_bite_id(row) for row in rows[:N]]


if __name__ == "__main__":
    res = get_most_complex_bites()
    print(res)
