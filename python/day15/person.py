class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    

class Employee(Person):

    def display(self,empId):
        self.empId = empId


emp = Employee("siva",21)

emp.display(1)
print(f"Name:{emp.name}")
print(f"Age:{emp.age}")
print(f"employee Id:{emp.empId}")