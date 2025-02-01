from datetime import date, time
from decimal import Decimal
from typing import Any

from pydantic import BaseModel, Field


class Account(BaseModel):
    id: str
    name: str
    balance: Decimal = Field(decimal_places=2)
    currency: str

    def dict(self, *args, **kwargs) -> dict[str, Any]:
        d = super().dict(*args, **kwargs)
        d['balance'] = float(d['balance'])
        return d


class Category(BaseModel):
    id: str
    name: str
    parent_id: str | None


class Transaction(BaseModel):
    id: str
    date: date
    time: time
    amount: Decimal = Field(decimal_places=2)
    account_id: str
    category_id: str
    description: str

    def dict(self, *args, **kwargs) -> dict[str, Any]:
        d = super().dict(*args, **kwargs)
        d['amount'] = float(d['amount'])
        return d
