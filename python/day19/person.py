class Person:
    def __init__(self,name):
        self._name = name


class Student(Person):
    def display(self):
        print(self._name)

stu = Student("swetha")
stu.display()