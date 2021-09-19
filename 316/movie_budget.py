from collections import defaultdict
from datetime import date
from typing import Dict, Sequence, NamedTuple


class MovieRented(NamedTuple):
    title: str
    price: int
    date: date


RentingHistory = Sequence[MovieRented]
STREAMING_COST_PER_MONTH = 12
STREAM, RENT = "stream", "rent"


def rent_or_stream(
    renting_history: RentingHistory,
    streaming_cost_per_month: int = STREAMING_COST_PER_MONTH,
) -> Dict[str, str]:
    """Function that calculates if renting movies one by one is
    cheaper than streaming movies by months.

    Determine this PER MONTH for the movies in renting_history.

    Return a dict of:
    keys = months (YYYY-MM)
    values = 'rent' or 'stream' based on what is cheaper

    Check out the tests for examples.
    """
    movie_months = defaultdict(list)

    for movie in renting_history:
        key = f"{movie.date.year}-{movie.date.month}"
        movie_months[key].append(movie.price)

    return {
        k: STREAM if (sum(v) > STREAMING_COST_PER_MONTH) else RENT
        for k, v in movie_months.items()
    }
