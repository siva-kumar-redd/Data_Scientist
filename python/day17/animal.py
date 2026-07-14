class Animal:
    def make_sound(self):
        print("This is animal sound")

class Dog(Animal):
    def make_sound(self):
        print("Dog: Bark")


class Cat(Animal):
    def make_sound(self):
        print("Cat: Meow")


class Cow(Animal):
    def make_sound(self):
        print("Cow: Moo")


animals = [Dog(),Cat(),Cow()]

for animal in animals:
    animal.make_sound()

