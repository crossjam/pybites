from collections import defaultdict
import os
from urllib.request import urlretrieve

from bs4 import BeautifulSoup


# prep data
tmp = os.getenv("TMP", "/tmp")
page = "us_holidays.html"
holidays_page = os.path.join(tmp, page)
urlretrieve(f"https://bites-data.s3.us-east-2.amazonaws.com/{page}", holidays_page)

with open(holidays_page) as f:
    content = f.read()

holidays = defaultdict(list)


def get_us_bank_holidays(content=content):
    """Receive scraped html output, make a BS object, parse the bank
    holiday table (css class = list-table), and return a dict of
    keys -> months and values -> list of bank holidays"""

    holidays = defaultdict(list)

    doc = BeautifulSoup(content, "html.parser")
    table = doc.find_all("table", class_="list-table")[0]
    for holiday, datetime in [
        (next(el.parent("a")[0].stripped_strings), el.parent("time")[0]["datetime"])
        for el in table("td")
        if "style" in el.attrs and el["style"] == "white-space: nowrap"
    ]:
        month = datetime.split("-")[1]
        holidays[month].append(holiday)

    print(holidays)
    return holidays
