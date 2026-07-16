class Product:
    def __init__(self,price):
        self.__price = price
    
    @property
    def price(self):
        return self.__price


prod = Product(500)

print(prod.price)