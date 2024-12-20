# E_library_API
A RESTful API for managing books, users, and borrow requests in an online library system.


## Prerequisites
- Python 3.12.6 
- pip (Python package installer)

  
## Installation
Clone the repository:
   -git clone https://github.com/Ughanzeisaac/E_library_API.git
   cd e-library-api
Create and activate a virtual environment:
   -python3 -m venv venv
   -venv\Scripts\activate
Install dependencies:
   -pip install -r requirements.txt
   
   
## Running the Application
To start the development server:
   -uvicorn main:app --reload
The API will be available at (http://localhost:8000).
The API documentation will be available at (http://localhost:8000/docs).


## Running Tests
To run the tests:
   -pytest
To test individual modules:
   -pytest tests/test_books.py
   -pytest tests/test_users.py
   -pytest tests/test_borrow.py
   

   
## Usage -User

**POST /Users** - Create a new user
   -http://localhost:8000/docs#/Users/create_user_users__post

**GET /Users** - List of users
   -http://localhost:8000/docs#/Users/get_users_users__get

**GET /Users** - List of users by Id
   -http://localhost:8000/docs#/Users/get_user_users__user_id__get

**PUT /Users** - Update a user by Id
  -http://localhost:8000/docs#/Users/update_user_users__user_id__put

**DELETE /Users** - Delete a user by Id
  -http://localhost:8000/docs#/Users/delete_user_users__user_id__delete

**PATCH /Users** - Update a user by Id 
  -http://localhost:8000/docs#/Users/deactivate_user_users__user_id__patch


## Usage -Books

**POST /books** - create a book 
   -http://localhost:8000/docs#/Books/create_book_books__post

**GET /books** - List all available books:
   -http://localhost:8000/docs#/Books/get_books_books__get
   
**PUT /books** - upadate a book by Id
   -http://localhost:8000/docs#/Books/update_book_books__book_id__put
   
**DELETE /books** - Delete a book by Id
   -http://localhost:8000/docs#/Books/delete_book_books__book_id__delete
   
**PATCH /books** - Mark a book Unavaliable by Id
-http://localhost:8000/docs#/Books/mark_book_unavailable_books__book_id__unavailable_patch


## Usage -Borrow Books

**POST / borrow** - borrow a book
  -http://localhost:8000/docs#/Borrow%20Books/borrow_book_borrow__post

**POST / borrow** - Return a book
  -http://localhost:8000/docs#/Borrow%20Books/return_book_return__post

**GET / borrow** - list of all borrow records
   -http://localhost:8000/docs#/Borrow%20Books/get_all_borrow_records_borrow__get

**GET / borrow** - List of all borrow records by Id
   -http://localhost:8000/docs#/Borrow%20Books/get_borrow_records_borrow__user_id__get
   

  



   


  

  
   
  



