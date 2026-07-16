class Student:
    def __init__(self,marks):
        self.__marks = marks
    
    def get_marks(self):
        return self.__marks


stu = Student(45)

print(stu.get_marks())