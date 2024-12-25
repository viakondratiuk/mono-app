from datetime import date, time
from decimal import Decimal
from pydantic import BaseModel, Field


class Transaction(BaseModel):
    date: date
    time: time
    # TODO: How to return the amount as float?
    amount: Decimal = Field(decimal_places=2)
    card: str
    category: str
    description: str
