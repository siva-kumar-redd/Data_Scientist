class Student:
    school_name = "ABC Public School"

    def __init__(self,name,roll_no):
        self.name = name
        self.roll_no = roll_no

    
    @classmethod
    def change_college_name(cls,new_name):
        cls.school_name = new_name

student1 = Student("siva",15)
student2 = Student('venky',17)

Student.change_college_name("XYZ Public School")
print(student1.school_name,"student name:",student1.name,"roll no:",student1.roll_no)
print(student2.school_name,"student name:",student2.name,"roll no: ",student2.roll_no)