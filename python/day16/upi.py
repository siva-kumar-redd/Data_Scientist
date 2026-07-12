class Payment:
    def pay(self):
        print("processing payment")


class Upi(Payment):
    def pay(self):
        super().pay()
        print("Processing UPI Payment")

class CreditCard(Upi):
    def pay(self):
        super().pay()
        print("Processing Credit Card Payment")


credit = CreditCard()
credit.pay()