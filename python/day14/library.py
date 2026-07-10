class Library:
    def __init__(self,book_name,author,price):
        self.book_name = book_name
        self.author = author
        self.price = price

    def display_details(self):
        print(self.book_name)
        print(self.author)
        print(self.price)


lib1 = Library("python","kohn",2500)
lib2 = Library('ml',"lyth",3500)

lib1.display_details()
lib2.display_details()