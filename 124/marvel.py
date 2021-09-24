from collections import Counter, namedtuple, defaultdict
import csv
import re

import requests

MARVEL_CSV = "https://raw.githubusercontent.com/pybites/marvel_challenge/master/marvel-wikia-data.csv"  # noqa E501

Character = namedtuple("Character", "pid name sid align sex appearances year")


# csv parsing code provided so this Bite can focus on the parsing


def _get_csv_data():
    """Download the marvel csv data and return its decoded content"""
    with requests.Session() as session:
        return session.get(MARVEL_CSV).content.decode("utf-8")


def load_data():
    """Converts marvel.csv into a sequence of Character namedtuples
    as defined above"""
    content = _get_csv_data()
    reader = csv.DictReader(content.splitlines(), delimiter=",")
    for row in reader:
        name = re.sub(r"(.*?)\(.*", r"\1", row["name"]).strip()
        yield Character(
            pid=row["page_id"],
            name=name,
            sid=row["ID"],
            align=row["ALIGN"],
            sex=row["SEX"],
            appearances=row["APPEARANCES"],
            year=row["Year"],
        )


characters = list(load_data())


# start coding


def most_popular_characters(characters=characters, top=5):
    """Get the most popular character by number of appearances,
    return top n characters (default 5)
    """
    appearances = Counter()
    for character in characters:
        if not character.appearances:
            continue

        appearances.update(
            {(character.pid, character.name.strip()): int(character.appearances)}
        )

    return [p[0][1] for p in appearances.most_common(top)]


most_popular_characters()


def max_and_min_years_new_characters(characters=characters):
    """Get the year with most and least new characters introduced respectively,
    use either the 'FIRST APPEARANCE' or 'Year' column in the csv
    characters, or the 'year' attribute of the namedtuple, return a tuple
    of (max_year, min_year)
    """

    appearances = Counter(
        [character.year for character in characters if character.year]
    )
    print((appearances.most_common()[0], appearances.most_common()[-1]))

    return (appearances.most_common()[0][0], appearances.most_common()[-1][0])


max_and_min_years_new_characters()


def get_percentage_female_characters(characters=characters):
    """Get the percentage of female characters as percentage of all genders
    over all appearances.
    Ignore characters that don't have gender ('sex' attribue) set
    (in your characters data set you should only have Male, Female,
    Agender and Genderfluid Characters.
    Return the result rounded to 2 digits
    """

    appearances = Counter([character.sex for character in characters if character.sex])

    total_appearances = sum(appearances.values())

    print(round((appearances["Female Characters"] / total_appearances) * 100, 2))
    return round(appearances["Female Characters"] / total_appearances * 100, 2)


get_percentage_female_characters()
