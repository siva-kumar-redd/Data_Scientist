class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author


book = Book("python","venky")

print(book.title)
print(book.author)