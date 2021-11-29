from itertools import zip_longest


JAN_1986 = """    January 1986
Su Mo Tu We Th Fr Sa
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30 31
"""


def grouper(iterable, n, fillvalue=None):
    "Collect data into non-overlapping fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def cal_line_chunks(line):
    return ["".join(v).strip() for v in list(grouper(line, 3, " "))]


def get_weekdays(calendar_output):
    """Receives a multiline Unix cal output and returns a mapping (dict) where
    keys are int days and values are the 2 letter weekdays (Su Mo Tu ...)"""
    cal_lines = calendar_output.splitlines()

    days = cal_line_chunks(cal_lines[1])

    kvs = []
    for line in cal_lines[2:]:
        pairs = [
            (int(day_num.strip()), day)
            for day_num, day in zip(cal_line_chunks(line), days)
            if day_num.strip()
        ]
        kvs.extend(pairs)

    return dict(kvs)


if __name__ == "__main__":
    print(get_weekdays(JAN_1986))
