from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
def test_add():
    response = client.post("/api/v1/add", json={"a": 2, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 5}
def test_subtract():
    response = client.post("/api/v1/subtract", json={"a": 5, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 2}
def test_multiply():
    response = client.post("/api/v1/multiply", json={"a": 2, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 6}
def test_divide():
    response = client.post("/api/v1/divide", json={"a": 6, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 2}
    response = client.post("/api/v1/divide", json={"a": 6, "b": 0})
    assert response.status_code == 400
    assert response.json() == {"detail": "Division by zero is not allowed."}