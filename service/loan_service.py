from dataclasses import dataclass
from datetime import datetime
from models.book import Book
from models.loan import Loan
from repositories.book_repository import BookRepository
from repositories.loan_repository import LoanRepository
from repositories.member_repository import MemberRepository
from utilitys.input_helps import LybraryError


@dataclass
class LoanService:

    member_repository : MemberRepository
    loan_repository : LoanRepository
    book_repository : BookRepository

    def borrow_a_book(self,loan_id:str,book_id:str,member_id:str):

        loan_book = self.book_repository.get_book_by_id(book_id)

        if self.loan_repository.get_loan_by_id(loan_id) is not None:
            raise LybraryError("This loan id is already taken. Try again.")

        if self.book_repository.get_book_by_id(book_id) is None:
            raise LybraryError("Book is does not exist")

        if self.member_repository.get_member_by_id(member_id) is None:
            raise LybraryError("Member does not exist")

        loan = Loan(loan_id=loan_id,member_id=member_id,book_id=book_id)

        book = Book(book_id=loan_book.book_id,title=loan_book.title,author=loan_book.author,year=loan_book.year,owner_member_id=member_id)

        self.book_repository.update_books(book)

        self.loan_repository.add_loan(loan)

    def return_a_book(self,loan_id:str):

        current_loan = self.loan_repository.get_loan_by_id(loan_id)

        if current_loan is None:
            raise LybraryError("loan does not exist. Try again!")


        loan_book = self.book_repository.get_book_by_id(current_loan.book_id)


        if loan_book is None:
            raise LybraryError("Book does not exist")

        loan = Loan(loan_id=loan_id,member_id=current_loan.member_id,book_id=current_loan.book_id,returned_at=datetime.now())

        book = Book(book_id=loan_book.book_id,title=loan_book.title,author=loan_book.author,year=loan_book.year,owner_member_id=None)

        self.loan_repository.update_loan(loan)

        self.book_repository.update_books(book)

    def get_active_loan(self):

        active_loans = self.loan_repository.get_active_loans()

        for loan in active_loans:
            print(f"Loan ID: {loan.loan_id} | Member ID: {loan.member_id} | Book ID: {loan.book_id} | "
                  f"Borrowed at: {loan.borrowed_at} | Return at: {loan.returned_at}")










