class Book:


    def __init__(self, title, author, is_borrowed=False):
      self.title = title
      self.author = author
      self.is_borrowed = is_borrowed

    def borrow_book(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return "book has been borrowed"
        else:
            return "you need to borrow a book"

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed=False
            return"Book is returned"
        else:
            return"book is not borrowed"




class member:
    def __init__(self, name):
      self.name = name
      self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            return "Borrow limit reached"
        #check to see if book is in borrowed book list
        if book in self.borrowed_books:
            return "Book already borrowed by this member"
        elif  book.is_borrowed:
            return "Book already borrowed by someone else"
        else:
            book.borrow_book()
            self.borrowed_books.append(book)
            return "Book borrowed successfully"

    def return_books(self,book):
        if book not in self.borrowed_books:
            return "Book not borrowed by this member"
        book.return_book()
        self.borrowed_books.remove(book)
        return "Book returned successfully"

print("You are about to borrow a book.")
name=input("Enter your name: ")
book1 = Book("1984", "George Orwell")
member1 = member("Alice")
m1=member(name)
m2=member(name)
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("The Catcher in the Rye", "J.D. Salinger")
book4 = Book("Pride and Prejudice", "Jane Austen")
book5= Book("Frankenstein", "Mary Shelley")
borrowing_book=m1.borrow_book(book1)
print(borrowing_book)
print(member1.borrow_book(book1))
returning_book=m1.return_books(book1)
print(returning_book)
print(member1.return_books(book1))
print(member1.borrow_book(book2))
print(member1.borrow_book(book3))
print(member1.borrow_book(book4))
print(member1.borrow_book(book5))

member2 = member("Bob")
print(member2.borrow_book(book1))