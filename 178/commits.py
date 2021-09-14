from collections import Counter
import os
import re

from urllib.request import urlretrieve

from dateutil.parser import parse

commits = os.path.join(os.getenv("TMP", "/tmp"), "commits")
urlretrieve("https://bites-data.s3.us-east-2.amazonaws.com/git_log_stat.out", commits)

# you can use this constant as key to the yyyymm:count dict
YEAR_MONTH = "{y}-{m:02d}"

RGX_EXTRACT = re.compile(
    r"^Date:\s+(.+) \| \d+ files? changed,(?: (\d+) insertions)?.+(?: (\d+) deletions)?"
)


def get_min_max_amount_of_commits(
    commit_log: str = commits, year: int = None
) -> (str, str):
    """
    Calculate the amount of inserts / deletes per month from the
    provided commit log.

    Takes optional year arg, if provided only look at lines for
    that year, if not, use the entire file.

    Returns a tuple of (least_active_month, most_active_month)
    """

    tally = Counter()
    for line in open(commit_log).read().splitlines():
        res = RGX_EXTRACT.search(line)
        dt_str, inserts_str, deletes_str = res.groups()

        dt = parse(dt_str)
        inserts = int(inserts_str) if inserts_str else 0
        deletes = int(deletes_str) if deletes_str else 0
        dt_key = YEAR_MONTH.format(y=dt.year, m=dt.month)

        if year and dt.year != year:
            continue
        tally.update({dt_key: inserts + deletes})

    results = (tally.most_common()[-1][0], tally.most_common()[0][0])
    return results


print(get_min_max_amount_of_commits())
