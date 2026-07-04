class Employee:
    company = "Google"

    def __init__(self,emp_name):
        self.emp_name = emp_name


    def __str__(self):
        return f"company: {self.company}\nname: {self.emp_name}"


emp1 = Employee("siva")
emp2 = Employee("kiran")


print(emp1)
print(emp2)