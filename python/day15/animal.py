class Animal:
    def eat(self):
        print("this is parent class")

class Dog(Animal):
    pass


dog = Dog()


dog.eat()