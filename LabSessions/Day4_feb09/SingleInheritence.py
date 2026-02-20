class SavingAccount:
    def __init__(self, acc_num, balance):
        self.acc_num = acc_num
        self.balance = balance

    def deposit(self, amt):
        self.balance = self.balance + amt
        print("Amount deposited:", amt)
        print("Balance is:", self.balance)


class AddInterest(SavingAccount):
    def add_interest(self, rate):
        interest = (self.balance * rate) / 100
        self.balance = self.balance + interest
        print("Interest added:", interest)
        print("Final balance:", self.balance)


a = AddInterest(12345, 500)
a.deposit(500)
a.add_interest(5)


# Level 1 (Base class)
class Account:
    def __init__(self, acc_no):
        self.acc_no = acc_no

    def show_account(self):
        print("Account Number:", self.acc_no)


# Level 2 (Intermediate class)
class SavingAccount(Account):
    def __init__(self, acc_no, balance):
        Account.__init__(self, acc_no)
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Deposited:", amount)
        print("Balance:", self.balance)


# Level 3 (Child class)
class SavingAccountWithInterest(SavingAccount):
    def add_interest(self, rate):
        interest = (self.balance * rate) / 100
        self.balance = self.balance + interest
        print("Interest added:", interest)
        print("Final Balance:", self.balance)


# Object creation
a = SavingAccountWithInterest(12345, 1000)
a.show_account()
a.deposit(500)
a.add_interest(5)
