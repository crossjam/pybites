from collections import Counter


def major_n_minor(numbers):
    """
    Input: an array with integer numbers
    Output: the majority and minority number
    """

    counts = Counter(numbers)

    ranks = counts.most_common()
    return (ranks[0][0], ranks[-1][0])


if __name__ == "__main__":
    print(major_n_minor([1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5]))
