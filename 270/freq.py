from collections import defaultdict


def freq_digit(num: int) -> int:
    rem = num
    counts = defaultdict(int)

    max_count, max_digit = 0, -1

    while rem:
        digit = rem % 10
        counts[digit] = counts[digit] + 1
        if max_count <= counts[digit]:
            max_digit, max_count = digit, counts[digit]
        rem = rem // 10

    return max_digit


print(freq_digit(177))
