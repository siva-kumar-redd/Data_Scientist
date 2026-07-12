class Account:
    def __init__(self,account_number,holder_name):
        self.account_number = account_number
        self.holder_name = holder_name
    
    def display(self):
        print("Account number:",self.account_number)
        print("Account holder name:",self.holder_name)


class SavingsAccount(Account):
    def __init__(self,account_number,holder_name,interest_rate):
        super().__init__(account_number,holder_name)
        self.interest_rate = interest_rate
    
    def display(self):
        super().display()
        print("interest rate:",self.interest_rate)


save = SavingsAccount(1,"siva",5)
save.display()