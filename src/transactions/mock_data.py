from datetime import date, time
from decimal import Decimal
from .models import Transaction

MOCK_TRANSACTIONS = [
    Transaction(
        date=date(2024, 3, 20),
        time=time(10, 30),
        amount=Decimal("123.45"),
        card="*1234",
        category="Groceries",
        description="Supermarket purchase",
    ),
    Transaction(
        date=date(2024, 3, 20),
        time=time(15, 45),
        amount=Decimal("45.00"),
        card="*5678",
        category="Transportation",
        description="Uber ride",
    ),
    Transaction(
        date=date(2024, 3, 19),
        time=time(9, 15),
        amount=Decimal("8.50"),
        card="*1234",
        category="Coffee",
        description="Morning coffee",
    ),
]
