class Author:
    def __init__(self, FullName):
        self.fullname = FullName
        
class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author.fullname
        
    def get_info(self):
        return f"Book: {self.name}, Author: {self.author}"
    

a = Author("Alisher Navoiy")
b = Book("Xamsa", a)
print(b.get_info())