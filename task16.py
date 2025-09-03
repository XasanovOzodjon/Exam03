class Account:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Xisob yetarli emas")
    
    @property
    def show_balanse(self):
        return self.balance

class SavingsAccount(Account):
    def __init__(self, balance, interest_rate):
        super().__init__(balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate

class CheckingAccount(Account):
    pass


s = SavingsAccount(1000, 0.05)
s.deposit(500)
print(s.calculate_interest())

d = CheckingAccount(900)
d.deposit(200)
print(d.show_balanse)
