from fastapi.testclient import TestClient
from main import app, status
from datetime import date, timedelta


client = TestClient(app)



def test_borrow_book():
    user_response = client.post("/users/", json={"name": "Zion Nweke", "email": "zion@gmail.com"})
    user_id = user_response.json()["id"]

    
    book_response = client.post("/books/", json={"title": "The Raven", "author": "Edger Allan Poe"})
    book_id = book_response.json()["id"]

    
    borrow_date = date.today()
    return_date = borrow_date + timedelta()


    borrow_response = client.post("/borrow/", json={
        "user_id": user_id,
        "book_id": book_id,
        "borrow_date": borrow_date.isoformat(),  
        "return_date": return_date.isoformat()   
    })

    
    assert borrow_response.status_code == status.HTTP_201_CREATED
