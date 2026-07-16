class Employee:
    def __init__(self,__salary):
        self.__salary = __salary

    def show_salary(self):
        print(self.__salary)


emp = Employee(25000)
emp.show_salary()