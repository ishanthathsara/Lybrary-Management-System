from abc import ABC, abstractmethod
from typing import Optional, List

from models.member import Member


class MemberRepository(ABC):

    @abstractmethod
    def add_member(self,member:Member) -> None:
        pass

    @abstractmethod
    def get_member_by_id(self,member_id) -> Optional[Member]:
        pass

    @abstractmethod
    def get_all_members(self) -> List[Member]:
        pass

    @abstractmethod
    def load_member(self) -> None:
        pass

    @abstractmethod
    def save_member(self) -> None:
        pass