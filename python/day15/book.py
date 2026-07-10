class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

class Ebook(Book):
    def __init__(self,title,author,file_size):
        super().__init__(title,author)
        self.file_size = file_size


ebook = Ebook("python","venky",25)

print(ebook.title)
print(ebook.author)
print(ebook.file_size)

