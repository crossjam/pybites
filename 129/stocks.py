import requests

from collections import Counter

STOCK_DATA = "https://bites-data.s3.us-east-2.amazonaws.com/stocks.json"

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(STOCK_DATA).json()


# your turn:


def _cap_str_to_mln_float(cap):
    """If cap = 'n/a' return 0, else:
    - strip off leading '$',
    - if 'M' in cap value, strip it off and return value as float,
    - if 'B', strip it off, multiply by 1,000 and return
      value as float"""

    if cap == "n/a":
        return 0
    elif cap.endswith("M"):
        return float(cap[1:-1])
    elif cap.endswith("B"):
        return float(cap[1:-1]) * 1000.0


def get_industry_cap(industry):
    """Return the sum of all cap values for given industry, use
    the _cap_str_to_mln_float to parse the cap values,
    return a float with 2 digit precision"""
    return round(
        sum(
            [
                _cap_str_to_mln_float(company["cap"])
                for company in data
                if company["industry"] == industry
            ]
        ),
        2,
    )


def get_stock_symbol_with_highest_cap():
    """Return the stock symbol (e.g. PACD) with the highest cap, use
    the _cap_str_to_mln_float to parse the cap values"""
    return max(data, key=lambda c: _cap_str_to_mln_float(c["cap"]))["symbol"]


def get_sectors_with_max_and_min_stocks():
    """Return a tuple of the sectors with most and least stocks,
    discard n/a"""
    counts = Counter(
        [company["sector"] for company in data if company["sector"] != "n/a"]
    )
    return (counts.most_common()[0][0], counts.most_common()[-1][0])
