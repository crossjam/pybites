import json


def get_movie_data(files: list) -> list:
    """Parse movie json files into a list of dicts"""
    movies = []
    for file_name in files:
        with open(file_name, "r") as in_file:
            movies.append(json.load(in_file))
    return movies


def get_single_comedy(movies: list) -> str:
    """return the movie with Comedy in Genres"""
    for movie in movies:
        if "Comedy" in movie["Genre"]:
            return movie["Title"]


def get_movie_most_nominations(movies: list) -> str:
    """Return the movie that had the most nominations"""

    def movie_nominations(movie):
        awards = movie["Awards"]
        wins, nominations = awards.split(" & ")
        num_nominations = int(nominations.split(" ", 1)[0])
        return num_nominations

    return max(
        [(movie_nominations(movie), movie["Title"]) for movie in movies],
        key=lambda p: p[0],
    )[1]


def get_movie_longest_runtime(movies: list) -> str:
    """Return the movie that has the longest runtime"""

    def movie_runtime(movie):
        runtime_str = movie["Runtime"]
        return int(runtime_str.split(" ", 1)[0])

    return max(
        [(movie_runtime(movie), movie["Title"]) for movie in movies], key=lambda p: p[0]
    )[1]
