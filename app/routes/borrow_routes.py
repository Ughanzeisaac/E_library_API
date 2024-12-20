from fastapi import APIRouter, HTTPException,status
from schemas.borrow_record import BorrowRecord, BorrowRecordCreate
from datetime import datetime
import datetime
from typing import List
from db.borrow_db import borrow_records_db
from db.user_db import users_db, user
from db.books_db import books_db, book


borrow_router = APIRouter()




@borrow_router.post("/borrow/", status_code=status.HTTP_201_CREATED)
def borrow_book(borrow_record: BorrowRecordCreate):
    user = next((u for u in users_db if u.id == borrow_record.user_id), None)
    book = next((b for b in books_db if b.id == borrow_record.book_id), None)

    if not user or not user.is_active:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Inactive or non-existing user")
    
    if not book or not book.is_available:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Book not available")

    if any(br.user_id == borrow_record.user_id and br.book_id == borrow_record.book_id and br.return_date is None for br in borrow_records_db):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already borrowed this book")

    
    new_borrow_record = BorrowRecord(id=len(borrow_records_db) + 1, **borrow_record.model_dump())
    borrow_records_db.append(new_borrow_record)
    
    book.is_available = False

    return new_borrow_record



@borrow_router.post("/return/", status_code=status.HTTP_201_CREATED)
def return_book(borrow_record_id: int):
    borrow_record = next((br for br in borrow_records_db if br.id == borrow_record_id and br.return_date is not None), None)
    
    if not borrow_record:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Borrow record not found or not yet returned")
    
    
    book = next((b for b in books_db if b.id == borrow_record.book_id), None)
    
    if book:
        book.is_available = True
    
    borrow_record.return_date = datetime.date.today()

    return {"message": "Book returned successfully"}




@borrow_router.get("/borrow/{user_id}", response_model=List[BorrowRecord], status_code=status.HTTP_200_OK)
def get_borrow_records(user_id: int):
    return [record for record in borrow_records_db if record.user_id == user_id]


@borrow_router.get("/borrow/", response_model=List[BorrowRecord], status_code=status.HTTP_200_OK)
def get_all_borrow_records():
    return borrow_records_db
