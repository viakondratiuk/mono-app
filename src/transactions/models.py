from datetime import date, time
from decimal import Decimal
from pydantic import BaseModel


class Transaction(BaseModel):
    date: date
    time: time
    amount: Decimal
    card: str
    category: str
    description: str
