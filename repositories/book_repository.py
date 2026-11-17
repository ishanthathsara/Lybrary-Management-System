from abc import ABC, abstractmethod
from typing import Optional, List

from models.book import Book


class BookRepository(ABC):

    @abstractmethod
    def add_book(self,book : Book) -> None:
        pass

    @abstractmethod
    def get_book_by_id(self,book_id) -> Optional[Book]:
        pass

    @abstractmethod
    def get_all_books(self) -> List[Book]:
        pass

    @abstractmethod
    def update_books(self,book : Book) -> None:
        pass

    @abstractmethod
    def load_book(self) -> None:
        pass

    @abstractmethod
    def save_books(self) -> None:
        pass



