from fastapi.testclient import TestClient
from main import api

client = TestClient(api)

def test_valid_id():
    response = client.get("/home")
    assert response.status_code == 200
    assert response.json() == {"fruit": "apple"}