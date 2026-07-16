class Laptop:
    def __init__(self,price):
        self.__price = price

    def set_price(self,price):
        if price<0:
            print("price should be greater than 0")
        else:
            self.__price = price
    
    def get_price(self):
        return self.__price


lap = Laptop(50000)

lap.set_price(-50)

print(lap.get_price())