class BankAccount:
    def __init__(self,account_number,customer_name,balance):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance
        
    def deposit(self,amount):
        if amount<0:
            print("deposit is not allowed")
        else:
            self.balance += amount

    def withdraw(self,amount):
        if amount>self.balance:
            print("insufficient funds")
        elif amount <= self.balance:
            print("withdraw successful")
        else:
            remaining_balance = self.balance-amount
    
    def show_balance(self):
        print(f"balance is {self.balance}")


customer1 = BankAccount(int(input("enter your account number")),input("enter your name"),int(input()))

customer1.deposit(-5)
customer1.withdraw(3000)
customer1.show_balance()