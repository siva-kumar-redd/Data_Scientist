class Person:
    def __init__(self,name):
        self.name = name


class Employee(Person):
    def __init__(self,name,employee_id):
        super().__init__(name)
        self.employee_id = employee_id

class Manager(Employee):
    def __init__(self,name,employee_id,department):
        super().__init__(name,employee_id)
        self.department = department


manager = Manager("siva",1,"IT")
print(manager.employee_id)
print(manager.name)
print(manager.department)