class Library:
    def __init__(self,library_name,author,price):
        self.library_name = library_name
        self.author = author
        self.price = price
    def display(self):
        print(self.library_name)
        print(self.author)
        print(self.price)
        
        

lib1 = Library("Python","john",2500)
lib2 = Library("ML","john joe",5000)
lib3 = Library("Data science","siva",2000)

lib1.display()
lib2.display()
lib3.display()