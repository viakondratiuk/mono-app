from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

from .mocks import AccountFactory, CategoryFactory, TransactionFactory
from .models import Account, Category, Transaction

app = FastAPI()


class AccountResponse(BaseModel):
    id: str
    name: str
    balance: float
    currency: str


class TransactionResponse(BaseModel):
    id: str
    date: str
    time: str
    amount: float
    account_id: str
    category_id: str
    description: str


@app.get("/accounts", response_model=List[AccountResponse])
def get_accounts():
    accounts = [AccountFactory.build() for _ in range(10)]
    return [
        {
            "id": account.id,
            "name": account.name,
            "balance": float(account.balance),
            "currency": account.currency,
        }
        for account in accounts
    ]


@app.get("/categories", response_model=List[Category])
def get_categories():
    return [CategoryFactory.build() for _ in range(10)]


@app.get("/transactions", response_model=List[TransactionResponse])
def get_transactions():
    transactions = [TransactionFactory.build() for _ in range(20)]
    return [
        {
            "id": t.id,
            "date": str(t.date),
            "time": str(t.time),
            "amount": float(t.amount),
            "account_id": t.account_id,
            "category_id": t.category_id,
            "description": t.description,
        }
        for t in transactions
    ]
