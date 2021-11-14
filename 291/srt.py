from datetime import timedelta, time, date, datetime
from typing import List

text1 = """
1
00:00:00,498 --> 00:00:02,827
Beautiful is better than ugly.

2
00:00:02,827 --> 00:00:06,383
Explicit is better than implicit.

3
00:00:06,383 --> 00:00:09,427
Simple is better than complex.
"""


def get_section_metrics(section: str) -> list:
    section_id, time_span, words = section.strip().splitlines()
    start_time_str, end_time_str = time_span.split(" --> ")
    start_time = time.fromisoformat(start_time_str[:8])
    end_time = time.fromisoformat(end_time_str[:8])

    time_delta = datetime.combine(date.min, end_time) - datetime.combine(
        date.min, start_time
    )
    # time_delta = end_time - start_time

    return [int(section_id), len(words.strip().split()) / time_delta.total_seconds()]


def get_srt_section_ids(text: str) -> List[int]:
    """Parse a caption (srt) text passed in and return a
    list of section numbers ordered descending by
    highest speech speed
    (= ratio of "time past:characters spoken")

    e.g. this section:

    1
    00:00:00,000 --> 00:00:01,000
    let's code

    (10 chars in 1 second)

    has a higher ratio then:

    2
    00:00:00,000 --> 00:00:03,000
    code

    (4 chars in 3 seconds)

    You can ignore milliseconds for this exercise.
    """

    metrics = [
        get_section_metrics(chunk.strip())
        for chunk in text.split("\n\n")
        if chunk.strip()
    ]

    return [m[0] for m in sorted(metrics, key=lambda m: m[1], reverse=True)]


if __name__ == "__main__":
    print(get_srt_section_ids(text1))
