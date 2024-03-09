class BankAccount:
    def __init__(self, accountId, bankName, bankId):
        self.accountId = accountId
        self.bankName = bankName
        self.bankId = bankId

    @property
    def accountId(self):
        return self._accountId

    @accountId.setter
    def accountId(self, accountId):
        self._accountId = accountId

    @property
    def bankName(self):
        return self._bankName

    @bankName.setter
    def bankName(self, bankName):
        self._bankName = bankName

    @property
    def bankId(self):
        return self._bankId

    @bankId.setter
    def bankId(self, bankId):
        self._bankId = bankId

    def __str__(self):
        return f"BankAccount: accountId={self.accountId}, bankName={self.bankName}, bankId={self.bankId}"

    def deposit(self, amount):
        deposited = False
        return deposited
