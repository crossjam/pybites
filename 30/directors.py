import csv
import statistics

from collections import defaultdict, namedtuple
import os
from urllib.request import urlretrieve

BASE_URL = "https://bites-data.s3.us-east-2.amazonaws.com/"
TMP = os.getenv("TMP", "/tmp")

fname = "movie_metadata.csv"
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)
urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple("Movie", "title year score")


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""

    movies = defaultdict(list)

    with open(local, "r", newline="") as in_file:
        rdr = csv.DictReader(in_file)
        for row in rdr:
            director_name = row.get("director_name", "")
            movie_title = row.get("movie_title", "")
            title_year = int(row["title_year"]) if row["title_year"] else 1900
            imdb_score = float(row["imdb_score"])

            if title_year < 1960:
                continue

            movie = Movie(movie_title, title_year, imdb_score)
            movies[director_name].append(movie)

    return movies


def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
    round the mean to 1 decimal place"""
    return round(statistics.mean([m.score for m in movies]), 1)


def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
    return a list of tuples (director, average_score) ordered by highest
    score in descending order. Only take directors into account
    with >= MIN_MOVIES"""

    scored_directors = [
        (director, calc_mean_score(films))
        for director, films in directors.items()
        if len(films) >= MIN_MOVIES
    ]
    scored_directors.sort(reverse=True, key=lambda p: p[1])
    return scored_directors
