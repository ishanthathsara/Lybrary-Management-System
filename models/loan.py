from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Loan:

    loan_id : str
    member_id : str
    book_id : str
    borrowed_at : datetime = field(default=datetime.now())
    returned_at : datetime | None = None

    


