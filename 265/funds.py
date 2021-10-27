import itertools

IMPOSSIBLE = "Mission impossible. No one can contribute."


def max_fund(village):
    if all([v < 0 for v in village]):
        print(IMPOSSIBLE)
        return (0, 0, 0)

    return max(
        [
            (sum(village[b:e]), b + 1, e)
            for b, e in itertools.combinations(range(len(village) + 1), 2)
        ]
    )


poverty = [0, -3, 2, 1, -7, 5, 3, -1, 6]
some = [2, -3, 2, 1, -7, -5, 3, -6, 18, 7, 13, 12]
extreme = [-1, -2, -3, -4, -5, -1, -2, -3]

if __name__ == "__main__":
    print(max_fund(poverty))
    print(max_fund(some))
    print(max_fund(extreme))
