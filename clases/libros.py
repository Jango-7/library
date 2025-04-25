class Book:
    def __init__(self, title, autor, isbn):
        self.title = title
        self.autor = autor
        self.isbn = isbn
        #self.available = False
    
    def update_info(self, available=True):
        if available:
            self.available = available
    
    def show_info(self):
        return f'Book: {self.title}\nAutor: {self.autor}\nISBN: {self.isbn}'