class Account:

    def __init__(self, name, start_balance=0):
        self.name = name
        self.start_balance = start_balance
        self._transactions = []

    @property
    def balance(self):
        return self.start_balance + sum(self._transactions)

    # add dunder methods below

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, position):
        return self._transactions[position]

    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __add__(self, val):
        if not isinstance(val, int):
            raise TypeError(f"not an int {val}")
        self._transactions.append(val)

    def __radd__(self, val):
        if not isinstance(val, int):
            raise TypeError(f"not an int {val}")
        self._transactions.append(val)

    def __sub__(self, val):
        if not isinstance(val, int):
            raise TypeError(f"not an int {val}")
        self._transactions.append(-val)

    def __rsub__(self, val):
        if not isinstance(val, int):
            raise TypeError(f"not an int {val}")
        self._transactions.append(-val)
        
    def __str__(self):
        return f"{self.name} account - balance: {self.balance}"

    
if __name__ == '__main__':
    checking = Account('Checking')
    saving = Account('Saving', 10)

    checking + 10
    print(checking)
    checking - 5
    print(checking)

    print(list(checking))
    
    checking + 'a'

