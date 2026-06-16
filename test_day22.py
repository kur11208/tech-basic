from fastapi.testclient import TestClient

from day22 import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "ETF test"}


def test_not_found():
    response = client.get("/not-found")
    assert response.status_code == 404
