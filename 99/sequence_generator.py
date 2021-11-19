import itertools
import string


def sequence_generator():

    for idx, char in itertools.cycle(enumerate(string.ascii_uppercase, 1)):
        yield idx
        yield char
