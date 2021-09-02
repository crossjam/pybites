from collections import Counter, defaultdict
import csv

import requests

from io import StringIO

CSV_URL = "https://raw.githubusercontent.com/pybites/SouthParkData/master/by-season/Season-{}.csv"  # noqa E501


def get_season_csv_file(season):
    """Receives a season int, and downloads loads in its
    corresponding CSV_URL"""
    with requests.Session() as s:
        download = s.get(CSV_URL.format(season))
        return download.content.decode("utf-8")


def get_num_words_spoken_by_character_per_episode(content):
    """Receives loaded csv content (str) and returns a dict of
    keys=characters and values=Counter object,
    which is a mapping of episode=>words spoken"""

    characters_spoken = defaultdict(Counter)

    with StringIO(content) as in_file:
        rdr = csv.DictReader(in_file)
        for row in rdr:
            words = row["Line"].split()
            characters_spoken[row["Character"]].update({row["Episode"]: len(words)})

    return characters_spoken
