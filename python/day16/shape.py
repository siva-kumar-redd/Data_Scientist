class Shape:
    def area(self):
        print("Area Calculation")


class Circle(Shape):
    def area(self):
        super().area()
        print("Area of Circle")


class Rectangle(Shape):
    def area(self):
        super().area()
        print("Area of Rectangle")


rectangle = Rectangle()
circle = Circle()
print("-------------------")
rectangle.area()
print("-------------------")
circle.area()