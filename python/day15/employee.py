class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Developer(Person):
    def __init__(self,name,age,language):
        super().__init__(name,age)
        self.language = language


class Tester(Person):
    def __init__(self,name,age,tool):
        super().__init__(name,age)
        self.tool = tool


develop = Developer("siva",21,"Java")
test = Tester("venky",22,"unit test")

print(f"name: {develop.name}\nage: {develop.age}\nprogramming language: {develop.language}")
print(f"name: {test.name}\nage: {test.age}\ntesting tool: {test.tool}")