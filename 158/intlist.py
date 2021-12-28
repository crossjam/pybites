from decimal import Decimal
from statistics import mean, median


class IntList(list):
    def _check_val(self, val):
        if isinstance(val, list) and all((isinstance(v, int) for v in val)):
            return True
        elif isinstance(val, (int, float, Decimal)):
            return True
        else:
            return False

    @property
    def mean(self):
        return mean(self)

    @property
    def median(self):
        return median(self)

    def append(self, val):
        if not self._check_val(val):
            raise TypeError("Invalid value")
        elif isinstance(val, Decimal):
            val = int(val)

        print(f"appending {val}")
        super().append(val)
        return self

    def __add__(self, val):
        if not self._check_val(val):
            raise TypeError("Invalid value")
        elif isinstance(val, Decimal):
            val = int(val)

        print(f"appending {val}")
        super().__add__(val)
        return self

    def __iadd__(self, val):
        if not self._check_val(val):
            raise TypeError("Invalid value")

        super().__iadd__(val)
        return self


if __name__ == "__main__":
    list1 = IntList([1, 3, 5])
    list1 += [1, 2, 3]

    print(list1)
    list1 += 4
