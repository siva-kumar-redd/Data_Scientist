class Animal:
    def __init__(self,sound):
        self._sound = sound


class Dog(Animal):
    def display(self):
        print(self._sound)

dog = Dog("boww")
dog.display()