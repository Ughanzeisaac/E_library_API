from fastapi import APIRouter, HTTPException, status
from schemas.book import Book, BookCreate, BookUpdate
from typing import List
from db.books_db import books_db



book_router = APIRouter()



@book_router.post("/books/", response_model=Book, status_code=status.HTTP_201_CREATED)
async def create_book(book: BookCreate):
    book_id = len(books_db) + 1
    new_book = Book(id=book_id, **book.model_dump())
    books_db.append(new_book)
    return new_book


@book_router.get("/books/", response_model=List[Book],status_code=status.HTTP_200_OK)
async def get_books():
    return books_db


@book_router.get("/books/{book_id}", response_model=Book,status_code=status.HTTP_200_OK)
async def get_book(book_id: int):
    book = next((b for b in books_db if b.id == book_id), None)
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return book


@book_router.put("/books/{book_id}", response_model=Book, status_code=status.HTTP_200_OK)
async def update_book(book_id: int, book_update: BookUpdate):
    book = next((b for b in books_db if b.id == book_id), None)
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    
    book_data = book.model_dump()
    book_data.pop("id", None)

    updated_data = book_update.model_dump(exclude_unset=True)
    book_data.update(updated_data)
    
    updated_book = Book(id=book.id, **book_data)
    books_db[books_db.index(book)] = updated_book
    return updated_book


@book_router.patch("/books/{book_id}/unavailable", status_code=status.HTTP_200_OK)
async def mark_book_unavailable(book_id: int):
    book = next((b for b in books_db if b.id == book_id), None)
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    
    book.is_available = False
    return {"message": "Book marked as unavailable"}



@book_router.delete("/books/{book_id}", status_code=status.HTTP_200_OK)
async def delete_book(book_id: int):
    book = next((b for b in books_db if b.id == book_id), None)
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "book not found")
    books_db.remove(book)
    return {"message": "Book deleted successfully"}
