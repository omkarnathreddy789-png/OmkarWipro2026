class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def __del__(self):
        print(f"BankAccount object with account number {self.account_number} is deleted.")

# Create and delete object
acc1 = BankAccount(12345, 1000)
del acc1
