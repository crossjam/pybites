from itertools import cycle
import sys
from time import time, sleep
import math

SPINNER_STATES = ["-", "\\", "|", "/"]  # had to escape \
STATE_TRANSITION_TIME = 0.1


def spinner(seconds):
    """Make a terminal loader/spinner animation using the imports above.
    Takes seconds argument = time for the spinner to run.
    Does not return anything, only prints to stdout."""

    cur_seconds = seconds
    states = cycle(SPINNER_STATES)

    while STATE_TRANSITION_TIME <= cur_seconds:
        sleep(STATE_TRANSITION_TIME)
        state = next(states)
        print(f"\r{state}", end="")  # flush
        cur_seconds -= STATE_TRANSITION_TIME


if __name__ == "__main__":
    spinner(0.2)
