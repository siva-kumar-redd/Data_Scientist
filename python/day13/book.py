class Book:
    def __init__(self,name,title):
        self.name = name
        self.title = title
    def display(self):
        print(self.name)
        print(self.title)


book = Book("siva","python")

book.display()