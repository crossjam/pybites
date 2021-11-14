import operator
from functools import reduce


def wc(file_):
    """Takes an absolute file path/name, calculates the number of
    lines/words/chars, and returns a string of these numbers + file, e.g.:
    3 12 60 /tmp/somefile
    (both tabs and spaces are allowed as separator)"""

    with open(file_, "r") as in_file:
        lines = in_file.readlines()
        chars = sum([len(line) for line in lines])
        words = reduce(operator.add, (len(line.split()) for line in lines), 0)

    return f"{len(lines)}\t{words}\t{chars}\t{file_}"


if __name__ == "__main__":
    # make it work from cli like original unix wc
    import sys

    print(wc(sys.argv[1]))
