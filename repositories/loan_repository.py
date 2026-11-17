from abc import ABC, abstractmethod
from typing import Optional, List

from models.loan import Loan


class LoanRepository(ABC):

    @abstractmethod
    def add_loan(self,loan : Loan) -> None:
        pass

    @abstractmethod
    def get_loan_by_id(self,loan_id) -> Optional[Loan]:
        pass

    @abstractmethod
    def get_all_loans(self) -> List[Loan]:
        pass

    @abstractmethod
    def update_loan(self, loan : Loan) -> None:
        pass

    @abstractmethod
    def get_active_loans(self) -> List[Loan]:
        pass

    @abstractmethod
    def load_loan(self) -> None:
        pass

    @abstractmethod
    def save_loan(self) -> None:
        pass
