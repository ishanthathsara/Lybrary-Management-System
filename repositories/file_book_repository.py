from typing import List, Optional, Dict

from models.book import Book
from repositories.book_repository import BookRepository


class FileBaseBookRepository(BookRepository):

    def __init__(self,file_name = "books.txt"):
        self.bookfile = file_name
        self.bookdict : Dict[str,Book] = {}
        self.load_book()

    def add_book(self, book: Book) -> None:
        self.bookdict[book.book_id] = book
        self.save_books()

    def get_book_by_id(self, book_id) -> Optional[Book]:

        return self.bookdict.get(book_id)

    def get_all_books(self) -> List[Book]:

        return list(self.bookdict.values())

    def update_books(self, book: Book) -> None:

        self.bookdict[book.book_id] = book
        self.save_books()

    def load_book(self) -> None:
        try:
            with open(self.bookfile, "r") as f:

                for book_details in f:

                    if not book_details.strip():
                        continue

                    line_list = book_details.strip().split("|")

                    book = Book(book_id=line_list[0],title=line_list[1],author=line_list[2],year=int(line_list[3]),owner_member_id=line_list[4])

                    self.bookdict[book.book_id] = book
        except FileNotFoundError as e:
            print({str(e)})

    def save_books(self) -> None:

        try:
            with open(self.bookfile, "w") as f:

                for book in self.bookdict.values():
                    f.write(f"{book.book_id}|{book.title}|{book.author}|{book.year}|{book.owner_member_id}\n")

        except FileNotFoundError as e:
            print(str(e))




