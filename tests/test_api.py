from fastapi.testclient import TestClient
from src.api import app

client = TestClient(app)


def test_get_accounts():
    response = client.get("/accounts")
    assert response.status_code == 200
    accounts = response.json()
    assert len(accounts) == 10
    assert all(isinstance(account["id"], str) for account in accounts)
    assert all(isinstance(account["name"], str) for account in accounts)
    assert all(isinstance(account["balance"], (int, float)) for account in accounts)


def test_get_categories():
    response = client.get("/categories")
    assert response.status_code == 200
    categories = response.json()
    assert len(categories) == 10
    assert all(isinstance(category["id"], str) for category in categories)
    assert all(isinstance(category["name"], str) for category in categories)


def test_get_transactions():
    response = client.get("/transactions")
    assert response.status_code == 200
    transactions = response.json()
    assert len(transactions) == 20
    assert all(isinstance(transaction["id"], str) for transaction in transactions)
    assert all(isinstance(transaction["amount"], (int, float)) for transaction in transactions)
    assert all(isinstance(transaction["category_id"], str) for transaction in transactions)
    assert all(isinstance(transaction["account_id"], str) for transaction in transactions)
    assert all(isinstance(transaction["description"], str) for transaction in transactions) 