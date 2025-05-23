from fastapi.testclient import TestClient
from app.main import app
from app.services.history_service import history_service

client = TestClient(app)

def test_add_v2():
    response = client.post("/api/v2/add", json={"a": 1, "b": 2})
    assert response.status_code == 200
    assert response.json() == {"result": 3}
def test_subtract_v2():
    response = client.post("/api/v2/subtract", json={"a": 5, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 2}
def test_multiply_v2():
    response = client.post("/api/v2/multiply", json={"a": 2, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 6}
def test_divide_v2():
    response = client.post("/api/v2/divide", json={"a": 6, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 2}
    # Test division by zero
    response = client.post("/api/v2/divide", json={"a": 6, "b": 0})
    assert response.status_code == 400
    assert response.json() == {"detail": "Division by zero is not allowed."}
def test_history_v2():
    history_service.clear_history()  # Clear history before the test
    client.post("/api/v2/add", json={"a": 1, "b": 2})
    client.post("/api/v2/subtract", json={"a": 5, "b": 3})
    
    response = client.get("/api/v2/history")
    assert response.status_code == 200
    history = response.json()
    assert isinstance(history, list)
    assert len(history) == 2
    assert history[0]["operation"] == "add"
    assert history[0]["a"] == 1
    assert history[0]["b"] == 2
    assert history[0]["result"] == 3
