from datetime import date, time
from decimal import Decimal

from pydantic import BaseModel, Field


class Account(BaseModel):
    id: str
    name: str
    balance: Decimal = Field(decimal_places=2)
    currency: str


class Category(BaseModel):
    id: str
    name: str
    parent_id: str | None


class Transaction(BaseModel):
    date: date
    time: time
    amount: Decimal = Field(decimal_places=2)
    account: Account
    category: Category
    description: str
