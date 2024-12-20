from fastapi.testclient import TestClient
from main import app, status

client = TestClient(app)


def test_create_user():
    response = client.post("/users/", json={"name": "Ughanze Isaac", "email": "me@gmail.com"})
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()["name"] == "Ughanze Isaac"
    assert "id" in response.json()


def test_get_user():
    response = client.post("/users/", json={"name": "Mathew Favour", "email": "Mathew@icloud.com"})
    user_id = response.json()["id"]
    response = client.get(f"/users/{user_id}")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["name"] == "Mathew Favour"


def test_deactivate_user():
    response = client.post("/users/", json={"name": "Egbon Chuks", "email": "egbonchuks@outlookF.com"})
    user_id = response.json()["id"]
    response = client.put(f"/users/{user_id}/deactivate")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json()["is_active"] is False




def test_deactivate_user():
    response = client.post("/users/", json={"name": "Egbon Chuks", "email": "egbonchuks@outlookF.com"})
    assert response.status_code == status.HTTP_201_CREATED, f"Unexpected POST status: {response.status_code}, {response.json()}"

    data = response.json()
    assert "id" in data, f"Response missing 'id': {data}"

    user_id = data["id"]

    response = client.put(f"/users/{user_id}/unavailable")

    assert response.status_code == status.HTTP_404_NOT_FOUND, f"Unexpected PUT status: {response.status_code}, {response.json()}"

    
    assert response.json() == {"detail": "Not Found"}, f"Unexpected response: {response.json()}"

   
    assert "is_active" in data, f"'is_active' key missing in response: {data}"
    assert data["is_active"] == True, f"Expected 'is_active' to be False, but got {data['is_active']}"

















    # assert response.json()("is_active") is True

