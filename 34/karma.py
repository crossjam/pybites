from collections import namedtuple
from datetime import datetime

Transaction = namedtuple("Transaction", "giver points date")
# https://twitter.com/raymondh/status/953173419486359552
Transaction.__new__.__defaults__ = (datetime.now(),)


class User:
    @property
    def karma(self):
        return sum((txn.points for txn in self._transactions))

    @property
    def points(self):
        return [txn.points for txn in self._transactions]

    @property
    def fans(self):
        return len({txn.giver for txn in self._transactions})

    def __init__(self, name):
        self.name = name
        self._transactions = []

    def __add__(self, txn):
        self._transactions.append(txn)

    def __str__(self):
        fans = {txn.giver for txn in self._transactions}
        fans_str = "fans" if len(fans) > 1 else "fan"
        return f"{self.name} has a karma of {self.karma} and {len(fans)} {fans_str}"
