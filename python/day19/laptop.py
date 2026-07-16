class Laptop:
    def __init__(self,__brand,__price):
        self.__brand = __brand
        self.__price = __price

    def display_details(self):
        print(self.__brand)
        print(self.__price)


lap = Laptop("HP",50000)
lap.display_details()