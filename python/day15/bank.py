class BankAccount:
    def __init__(self,account_holder_name,balance):
        self.account_holder_name = account_holder_name
        self.balance = balance

class SavingsAccount(BankAccount):
    def interest_rate(self,interest):
        self.interest = interest


saved = SavingsAccount("siva",1500)

saved.interest_rate(0.5)

print(f"account holder:{saved.account_holder_name}")
print(f"balance:{saved.balance}")
print(f"interest rate:{saved.interest_rate}")