import os
from pathlib import Path
from urllib.request import urlretrieve

from collections import defaultdict
import xml.etree.ElementTree as ET

# import the countries xml file
tmp = Path(os.getenv("TMP", "/tmp"))
countries = tmp / "countries.xml"

if not countries.exists():
    urlretrieve(
        "https://bites-data.s3.us-east-2.amazonaws.com/countries.xml", countries
    )


def get_income_distribution(xml=countries):
    """
    - Read in the countries xml as stored in countries variable.
    - Parse the XML
    - Return a dict of:
      - keys = incomes (wb:incomeLevel)
      - values = list of country names (wb:name)
    """

    distribution = defaultdict(list)
    doc = ET.parse(xml)
    root = doc.getroot()

    ns = {"wb": "http://www.worldbank.org"}

    countries = root.findall("wb:country", ns)
    for country in countries:
        country_name = country.find("wb:name", ns).text
        country_income_level = country.find("wb:incomeLevel", ns).text
        distribution[country_income_level].append(country_name)

    return distribution


if __name__ == "__main__":
    get_income_distribution()
