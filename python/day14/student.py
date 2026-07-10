class Student:
    school_name = "ABC Public School"

    def __init__(self,name,roll_no):
        self.name = name
        self.roll_no = roll_no

    


student1 = Student("siva",15)
student2 = Student('venky',17)


print(student1.school_name,"student name:",student1.name,"roll no:",student1.roll_no)
print(student2.school_name,"student name:",student2.name,"roll no: ",student2.roll_no)