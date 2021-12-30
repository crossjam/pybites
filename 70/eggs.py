from random import choice

COLORS = "red blue green yellow brown purple".split()


class EggCreator:
    def __init__(self, limit):
        self._limit = limit
        self._iterator = iter(range(self._limit))

    def __iter__(self):
        return self

    def __next__(self):
        try:
            next(self._iterator)
            color = choice(COLORS)
            return f"{color} egg"

        except StopIteration:
            raise


if __name__ == "__main__":
    ec = EggCreator(20)
    print(list(ec))
