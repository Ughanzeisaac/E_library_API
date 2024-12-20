from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class BorrowRecordBase(BaseModel):
    user_id: int
    book_id: int
    borrow_date: datetime
    return_date: datetime


class BorrowRecordCreate(BorrowRecordBase):
    pass


class BorrowRecord(BorrowRecordBase):
    id: int
