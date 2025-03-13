class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        return f"Book(title={self.title}, author={self.author})"


class BookCollection:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def __iter__(self):
        return BookIterator(self.books)


class BookIterator:
    def __init__(self, books):
        self.books = books
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.books):
            book = self.books[self.index]
            self.index += 1
            return book
        else:
            raise StopIteration


book1 = Book("Bible", "God")
book2 = Book("1984", "Gorge Orwell")
book3 = Book("The lord of the rings 1", "JRR. Tolkien")


book_collection = BookCollection()
book_collection.add_book(book1)
book_collection.add_book(book2)
book_collection.add_book(book3)

for book in book_collection:
    pass #print(book)

book_collection_iterator = iter(book_collection)
print(next(book_collection_iterator))
print(next(book_collection_iterator))
print(next(book_collection_iterator))
print(next(book_collection_iterator))