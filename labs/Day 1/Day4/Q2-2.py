class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)
        print("New Balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
            print("Remaining Balance:", self.balance)
        else:
            print("Insufficient Balance!")

# Test the methods
acc1 = BankAccount(12345, 1000)
acc1.deposit(500)
acc1.withdraw(300)
acc1.withdraw(1500)
