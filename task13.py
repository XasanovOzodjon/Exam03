from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass

class PayPalPayment(Payment):
    def pay(self, amaunt):
        print(f"Paid {amaunt} using PayPal")

class CardPayment(Payment):
    def pay(self, amaunt):
        print(f"Paid {amaunt} using Card")


p1 = PayPalPayment()
p2 = CardPayment()
p1.pay(100)
p2.pay(200)