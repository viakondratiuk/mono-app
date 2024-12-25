from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_transactions():
    response = client.get("/transactions/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0
    for transaction in response.json():
        assert "date" in transaction
        assert "time" in transaction
        assert "amount" in transaction
        assert "card" in transaction
        assert "category" in transaction
        assert "description" in transaction
