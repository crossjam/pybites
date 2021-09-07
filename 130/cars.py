from collections import Counter, defaultdict

import requests

CAR_DATA = "https://bites-data.s3.us-east-2.amazonaws.com/cars.json"

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(CAR_DATA).json()


# your turn:
def most_prolific_automaker(year):
    """Given year 'year' return the automaker that released
    the highest number of new car models"""
    years = defaultdict(lambda: Counter())

    for row in data:
        years[row["year"]].update({row["automaker"]: 1})

    return years[year].most_common(1)[0][0]


def get_models(automaker, year):
    """Filter cars 'data' by 'automaker' and 'year',
    return a set of models (a 'set' to avoid duplicate models)"""
    return set(
        [
            row["model"]
            for row in data
            if row["automaker"] == automaker and row["year"] == year
        ]
    )
