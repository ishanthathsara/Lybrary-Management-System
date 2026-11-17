from datetime import datetime
from typing import List, Optional, Dict

from models.loan import Loan
from repositories.loan_repository import LoanRepository


class FileBaseLoanRepository(LoanRepository):

    def __init__(self,file_name = "loans.txt"):
        self.loanfile = file_name
        self.loandict : Dict[str,Loan] = {}
        self.load_loan()

    def add_loan(self, loan: Loan) -> None:

        self.loandict[loan.loan_id] = loan
        self.save_loan()

    def get_loan_by_id(self, loan_id) -> Optional[Loan]:

        return self.loandict.get(loan_id)

    def get_all_loans(self) -> List[Loan]:

        return list(self.loandict.values())

    def update_loan(self, loan: Loan) -> None:

        self.loandict[loan.loan_id] = loan
        self.save_loan()

    def get_active_loans(self) -> List[Loan]:

        active_loan_list = []

        for loan in self.loandict.values():
            if loan.returned_at is None:
                active_loan_list.append(loan)

        return  list(active_loan_list)


    def load_loan(self) -> None:

        try:
            with open(self.loanfile, "r") as f:

                for detail_line in f:

                    if not detail_line.strip():
                        continue

                    line_list = detail_line.strip().split("|")

                    if line_list[4] == "None":
                        loan = Loan(loan_id=line_list[0], member_id=line_list[1], book_id=line_list[2],
                                    borrowed_at=datetime.strptime(line_list[3], "%Y-%m-%d %H:%M:%S.%f"),
                                    returned_at=None)
                        self.loandict[loan.loan_id] = loan

                    else:
                        loan = Loan(loan_id=line_list[0], member_id=line_list[1], book_id=line_list[2], borrowed_at=datetime.strptime(line_list[3], "%Y-%m-%d %H:%M:%S.%f"), returned_at=datetime.strptime(line_list[4], "%Y-%m-%d %H:%M:%S.%f"))
                        self.loandict[loan.loan_id] = loan

        except FileNotFoundError as e:
            print(str(e))

    def save_loan(self) -> None:

        try:
            with open(self.loanfile, "w") as f:

                for loan in self.loandict.values():
                    f.write(f"{loan.loan_id}|{loan.member_id}|{loan.book_id}|{loan.borrowed_at}|{loan.returned_at}\n")

        except FileNotFoundError as e:
            print(str(e))

