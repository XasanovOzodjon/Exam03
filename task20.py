class Library:
    def __init__(self):
        self.books = []
        self.borrow_books = []
        
    def add_book(self, name, author):
        temp_dic = {"name": name, "author": author}
        self.books.append(temp_dic)
        
    def borrow_book(self, name):
        for book in self.books:
            if name == book["name"]:
                self.borrow_books.append(book)
                self.books.remove(book)
                return f"You borrowed '{name}'"
        
        return f"Sorry, '{name}' is not available"
    
    def return_book(self, name):
        for book in self.borrow_books:
            if name == book["name"]:
                self.books.append(book)
                self.borrow_books.remove(book)
                return f"You returned '{name}'"
        return f"Bu kitobni bizdan olmagansiz"
                
                
lib = Library()
lib.add_book("1984", "George Orwell")
lib.add_book("Xamsa", "Alisher Navoiy")

print(lib.borrow_book("1984"))
print(lib.borrow_book("1984"))
print(lib.return_book("1984"))
