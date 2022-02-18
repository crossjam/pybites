from typing import List


def minimum_number(digits: List[int]) -> int:
    if not digits:
        return 0

    ordered_digits = sorted(list(set(digits)))

    return int("".join([f"{digit}" for digit in ordered_digits]))
