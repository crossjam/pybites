import csv
import io
from collections import Counter

import requests

CSV_URL = "https://bites-data.s3.us-east-2.amazonaws.com/community.csv"


def get_csv():
    """Use requests to download the csv and return the
    decoded content"""
    resp = requests.get(CSV_URL)
    return resp.text


def create_user_bar_chart(content):
    """Receives csv file (decoded) content and print a table of timezones
    and their corresponding member counts in pluses to standard output
    """

    rdr = csv.DictReader(io.StringIO(content))

    counts = Counter([r["tz"] for r in rdr])
    for k, v in counts.items():
        print(f"{k: <20} | {'+' * v}")
