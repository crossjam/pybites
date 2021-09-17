from csv import DictReader
import os
from urllib.request import urlretrieve
from collections import Counter

TMP = os.getenv("TMP", "/tmp")
LOGS = "bite_output_log.txt"
DATA = os.path.join(TMP, LOGS)
S3 = "https://bites-data.s3.us-east-2.amazonaws.com"
if not os.path.isfile(DATA):
    urlretrieve(f"{S3}/{LOGS}", DATA)


class BiteStats:
    def _load_data(self, data) -> list:
        with open(DATA) as in_file:
            rdr = DictReader(in_file)
            return [r for r in rdr]

    def __init__(self, data=DATA):
        self.rows = self._load_data(data)

    @property
    def number_bites_accessed(self) -> int:
        """Get the number of unique Bites accessed"""
        return len(set(r["bite"] for r in self.rows))

    @property
    def number_bites_resolved(self) -> int:
        """Get the number of unique Bites resolved (completed=True)"""
        return len(set(r["bite"] for r in self.rows if r["completed"] == "True"))

    @property
    def number_users_active(self) -> int:
        """Get the number of unique users in the data set"""
        return len(set(r["user"] for r in self.rows))

    @property
    def number_users_solving_bites(self) -> int:
        """Get the number of unique users that resolved
        one or more Bites"""
        return len(set(r["user"] for r in self.rows if r["completed"] == "True"))

    @property
    def top_bite_by_number_of_clicks(self) -> str:
        """Get the Bite that got accessed the most
        (= in most rows)"""
        counts = Counter((r["bite"] for r in self.rows))
        return counts.most_common(1)[0][0]

    @property
    def top_user_by_bites_completed(self) -> str:
        """Get the user that completed the most Bites"""
        counts = Counter((r["user"] for r in self.rows if r["completed"] == "True"))
        return counts.most_common(1)[0][0]
