class Animal:
    def eat(self):
        print("eat something")

class Dog(Animal):
    def bark(self):
        print("dog saying baww..")


class Cat(Animal):
    def meow(self):
        print("cat saying meow")


dog = Dog()
cat = Cat()

dog.eat()
dog.bark()

cat.eat()
cat.meow()