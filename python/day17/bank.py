class SavingsAccount:
    def calculate_interest(self):
        print("saving interest")


class CurrentAccount:
    def calculate_interest(self):
        print("current interest")


class SalaryAccount:
    def calculate_interest(self):
        print("salary interest")


interest = [SavingsAccount(),CurrentAccount(),SalaryAccount()]

for i in interest:
    i.calculate_interest()