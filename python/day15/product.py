class Product:
    def __init__(self,product_name,price):
        self.product_name = product_name
        self.price = price

class Electronics(Product):
    def __init__(self,product_name,price,Warranty):
        super().__init__(product_name,price)
        self.Warranty = Warranty

class Clothing(Product):
    def __init__(self,product_name,price,size):
        super().__init__(product_name,price)
        self.size = size


electro = Electronics("tv",25000,5)
cloth = Clothing("pant",2000,"XL")

print(f"product_name: {electro.product_name}\nprice: {electro.price}\nwarranty in years: {electro.Warranty}")
print(f"product_name: {cloth.product_name}\nprice: {cloth.price}\nsize: {cloth.size}")

