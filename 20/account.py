from copy import copy

class Account:

    def __init__(self):
        self._transactions = []

    @property
    def balance(self):
        return sum(self._transactions)

    def __add__(self, amount):
        self._transactions.append(amount)

    def __sub__(self, amount):
        self._transactions.append(-amount)

    # add 2 dunder methods here to turn this class 
    # into a 'rollback' context manager

    def __enter__(self):
        self._previous_transactions = copy(self._transactions)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_value is not None or self.balance < 0:
            self._transactions = self._previous_transactions
        self._previous_transactions = None

if __name__ == '__main__':
    account = Account()
    account + 3
    with account as acc:
        acc - 5

    assert account.balance == 3
    
    with account as acc:
        acc + 10
        acc - 3

    assert account.balance == 10
    
