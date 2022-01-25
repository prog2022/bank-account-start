import datetime
import sys

class bank_account:
    """A bank account with account id and owner.
       Transactions are recorded individually
    """

    def __init__(self, acctId, owner):
        self.acctId = acctId
        self.own = owner
        self.Transactions = []

    def dep(self,amt):
        """deposit to the bank account"""
        if amt <= 0:
            raise ValueError("Deposit must be positive amount")
        elif amt > 0:
            t = Transaction(self.acctId, "deposit", amt)
            Transactions.append(t)
    
    def wd(self,amt):
        """Withdraw money from the bank account."""
        if amt <= 0:
            raise ValueError("Withdraw amount must be positive")
        b = self.getBalance()
        if amt > b:
            raise TransactionError("Insufficient funds to withdraw "+str(amt))
        t = Transaction(self.acctId, "withdraw", -amt)
        Transactions.append(t)
    
    def getBalance(self):
        return sum([t.amount for t in self.Transactions])

class Transaction:
    """ Information about a transaction. """
    def __init__(self, type:str, amount:str):
        self.type = type
        self.amount = amount
        self.date = datetime.datetime.now()

class TransactionError(BaseException):
    """Exception class for transaction errors"""
    def __init__(self, message: str):
        super().__init__(message)
