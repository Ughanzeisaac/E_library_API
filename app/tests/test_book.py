from fastapi.testclient import TestClient
from main import app, status



client = TestClient(app)


def test_create_book():
    response = client.post("/books/", json={"title": "The Psychology of Money", "author": "Morgan Housel"})
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()["title"] == "The Psychology of Money"
    assert "id" in response.json()


def test_get_book():
    response = client.post("/books/", json={"title": "Think and Grow Rich", "author": "Napoleon Hill"})
    book_id = response.json()["id"]
    response = client.get(f"/books/{book_id}")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["title"] == "Think and Grow Rich"



def test_mark_book_unavailable():
    response = client.post("/books/", json={"title": "The Intelligent Investor", "author": "Benjamin Graham"})
    assert response.status_code == status.HTTP_201_CREATED, f"Unexpected POST status: {response.status_code}, {response.json()}"
    data = response.json()
    assert "id" in data, f"Response missing 'id': {data}"

    book_id = data["id"]

   
    response = client.patch(f"/books/{book_id}/unavailable") 
    assert response.status_code == status.HTTP_200_OK, f"Unexpected PATCH status: {response.status_code}, {response.json()}"
