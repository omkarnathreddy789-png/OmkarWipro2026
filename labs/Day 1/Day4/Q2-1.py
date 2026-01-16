class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance


acc1 = BankAccount(12345, 1000)
print("Account Number:", acc1.account_number)
print("Balance:", acc1.balance)
