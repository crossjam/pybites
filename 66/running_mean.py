from itertools import accumulate


def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
    returns a sequence of same length with the averages.
    You can assume all items in sequence are numeric."""
    for numerator, denominator in zip(
        accumulate(sequence), range(1, len(sequence) + 1)
    ):
        yield round(numerator / denominator, 2)


if __name__ == "__main__":
    print(list(running_mean([1, 2, 3])))
