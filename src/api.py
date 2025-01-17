from typing import List

from fastapi import FastAPI

from .mocks import AccountFactory, CategoryFactory, TransactionFactory
from .models import Account, Category, Transaction

app = FastAPI()


@app.get("/accounts", response_model=List[Account])
def get_accounts():
    return [AccountFactory.build() for _ in range(10)]


@app.get("/categories", response_model=List[Category])
def get_categories():
    return [CategoryFactory.build() for _ in range(10)]


@app.get("/transactions", response_model=List[Transaction])
def get_transactions():
    return [TransactionFactory.build() for _ in range(20)]
