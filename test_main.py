from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_return_one():
    response = client.get("/return_one")
    assert response.status_code == 200
    assert response.json() == {"number": 1}
