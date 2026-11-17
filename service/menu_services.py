from dataclasses import dataclass

from models.book import Book
from models.member import Member
from repositories.book_repository import BookRepository
from repositories.member_repository import MemberRepository
from utilitys.input_helps import LybraryError


@dataclass
class MenuService:

    book_repository : BookRepository
    member_repository : MemberRepository


    def list_all_books(self):

        for book in self.book_repository.get_all_books():
            print(f"Book id: {book.book_id} | Title: {book.title} | Author: {book.author} | Year: {book.year} | Book_lend_member_id: {book.owner_member_id}")

    def add_a_book(self,book_id:str,title:str,author:str,year:int):

        if self.book_repository.get_book_by_id(book_id) is not None:
            raise LybraryError("This book id is already taken. Try again!")

        book = Book(book_id=book_id,title=title,author=author,year=year)

        self.book_repository.add_book(book)

    def register_a_member(self,member_id:str,member_name:str):

        if self.member_repository.get_member_by_id(member_id) is not None:
            raise LybraryError("This member id is already taken")

        member = Member(member_id=member_id,name=member_name)

        self.member_repository.add_member(member)

    def list_members(self):

        for member in self.member_repository.get_all_members():
            print(f"Member ID: {member.member_id} | Member Name: {member.name}")












