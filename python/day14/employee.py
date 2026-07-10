class Employee:
    company_name = "ABC Technologies"
    def __init__(self,empId,empName):
        self.empId = empId
        self.empName = empName

    @classmethod
    def change_company_name(cls,new_company_name):
        cls.company_name = new_company_name


emp1 = Employee(1,"siva")
emp2 = Employee(2,"venky")

Employee.change_company_name("XYZ Technologies")

print(f"employee id: {emp1.empId} \nemployee name: {emp1.empName} \ncompany name: {emp1.company_name} \n")
print(f"employee id: {emp2.empId} \nemployee name: {emp2.empName} \ncompany name: {emp2.company_name} \n")