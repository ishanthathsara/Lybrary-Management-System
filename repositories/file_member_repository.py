from typing import List, Optional, Dict

from models.member import Member
from repositories.member_repository import MemberRepository


class FileBaseMemberRepository(MemberRepository):

    def __init__(self,file_name = "members.txt"):
        self.membersfile = file_name
        self.memberDict : Dict[str,Member] = {}
        self.load_member()

    def add_member(self, member: Member) -> None:

        self.memberDict[member.member_id] = member
        self.save_member()

    def get_member_by_id(self, member_id) -> Optional[Member]:

        return self.memberDict.get(member_id)

    def get_all_members(self) -> List[Member]:

        return list(self.memberDict.values())

    def save_member(self) -> None:

        try:
            with open(self.membersfile, "w") as f:

                for member in self.memberDict.values():
                    f.write(f"{member.member_id}|{member.name}\n")

        except FileNotFoundError as e:
            print(str(e))

    def load_member(self) -> None:

        try:
            with open(self.membersfile, "r") as f:

                for detail_line in f:

                    if not detail_line.strip():
                        continue

                    line_list = detail_line.strip().split("|")

                    member = Member(member_id=line_list[0],name=line_list[1])

                    self.memberDict[member.member_id] = member

        except FileNotFoundError as e:
            print(str(e))




