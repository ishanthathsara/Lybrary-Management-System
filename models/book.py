from dataclasses import dataclass


@dataclass
class Book:

    book_id : str
    title : str
    author : str
    year : int
    owner_member_id : str | None = None

    