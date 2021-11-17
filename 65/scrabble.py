import itertools
import os
import operator
import urllib.request

from functools import reduce

# PREWORK
TMP = os.getenv("TMP", "/tmp")
DICT = "dictionary.txt"
DICTIONARY = os.path.join(TMP, DICT)
urllib.request.urlretrieve(
    f"https://bites-data.s3.us-east-2.amazonaws.com/{DICT}", DICTIONARY
)

with open(DICTIONARY) as f:
    dictionary = set([word.strip().lower() for word in f.read().split()])


def get_possible_dict_words(draw):
    """Get all possible words from a draw (list of letters) which are
    valid dictionary words. Use _get_permutations_draw and provided
    dictionary"""

    global dictionary

    return [
        "".join(p).lower()
        for p in _get_permutations_draw(draw)
        if "".join(p).lower() in dictionary
    ]


def _get_permutations_draw(draw):
    """Helper to get all permutations of a draw (list of letters), hint:
    use itertools.permutations (order of letters matters)"""

    return reduce(
        operator.add,
        (list(itertools.permutations(draw, sz)) for sz in range(1, len(draw) + 1)),
        [],
    )


if __name__ == "__main__":
    draw = "T, I, I, G, T, T, L".split(", ")
    print(get_possible_dict_words(draw))
