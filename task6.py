class BankAccount:
    def __init__(self, balanse):
        self.__balanse = balanse
    
    def deposit(self,amount):
        if amount > 0:
            self.__balanse += amount
        else:
            raise(ValueError("Depazit 0 dan katta bolishi kerak"))
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balanse:
            self.__balanse -= amount
        else:
            raise(ValueError("Pul yetarli emas yoki noto'g'ri summa kiritildi"))

    def get_balance(self):
        return self.__balanse

acc = BankAccount(100)
acc.deposit(50)
acc.withdraw(30)
print(acc.get_balance())