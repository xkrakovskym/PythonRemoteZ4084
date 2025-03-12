from abc import ABC, abstractmethod

class Beverage(ABC):
    def __init__(self, payment_method):
        self.payment_method = payment_method

    @abstractmethod
    def purchase(self):
        pass


class Tea(Beverage):
    def __init__(self, payment_method, price):
        super().__init__(payment_method)
        self.price = price

    def purchase(self):
        print("Purchasing tea...")
        self.payment_method.pay(self.price)


class Coffee(Beverage):
    def __init__(self, payment_method, price):
        super().__init__(payment_method)
        self.price = price

    def purchase(self):
        print("Purchasing coffee...")
        self.payment_method.pay(self.price)


class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card.")


class Cash(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} in cash.")


class Bitcoin(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} with bitcoin.")


credit_card = CreditCard()
cash = Cash()
bitcoin = Bitcoin()

tea_with_credit = Tea(credit_card, 3.5)
coffee_with_cash = Coffee(cash, 4.0)
cappucino_with_bitcoin = Coffee(bitcoin, 5.5)

tea_with_credit.purchase()
coffee_with_cash.purchase()
cappucino_with_bitcoin.purchase()