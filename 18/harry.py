import os
import urllib.request

import re
import string

from collections import Counter

# data provided
tmp = os.getenv("TMP", "/tmp")
stopwords_file = os.path.join(tmp, "stopwords")
harry_text = os.path.join(tmp, "harry")
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/stopwords.txt", stopwords_file
)
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/harry.txt", harry_text
)


def get_harry_most_common_word():
    stopwords = set()
    counts = Counter()
    punct_strip_rgx = re.compile(r"[^a-z0-9\s]")

    with open(stopwords_file, "r") as in_file:
        stopwords = set([line.strip() for line in in_file if line.strip()])

    with open(harry_text, "r") as in_file:
        for line in in_file:
            line = line.strip()
            if not line:
                continue
            line = line.lower()
            line = punct_strip_rgx.sub("", line)
            counts.update([w for w in line.split() if w not in stopwords])

    return tuple(counts.most_common(1)[0])
