#Real World Situation: Library books

#File the classes are stored in: library.py

#File the code is stored in: main.py



#library.py
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False
    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            return f'"{self.title}" has been checked out'
        return f'"{self.title}" is already taken'
    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            return f'"{self.title}" has been returned'
        return f'"{self.title}" was not checked out'


class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
    def show_available_books(self):
        available = [book for book in self.books if not book.is_checked_out]
        if not available:
            return "No books are avaliable :("
        return "\n".join([f"{book.title} by {book.author}" for book in available])


#main.py
def main():
    # Create library
    my_library = Library()

    # Add books
    book1 = Book("Dog man", "Dav Pilky")
    book2 = Book("Captain underpants", "Dav Pilky")
    my_library.add_book(book1)
    my_library.add_book(book2)

    #shows avaliable books
    print("Availiable books:")
    print(my_library.show_available_books())

    #Book checkout
    print("\nChecking out a book:")
    print(book1.check_out())

    #trys to check book out again
    print(book1.check_out())

    #Shows avaliable vooks again
    print("\nAvailable Books After Checkout:")
    print(my_library.show_available_books())

    #Return book
    print("\nReturning the book:")
    print(book1.return_book())

    #final book list
    print("\nAvailable Books:")
    print(my_library.show_available_books())


# Run the program
if __name__ == "__main__":
    main()
