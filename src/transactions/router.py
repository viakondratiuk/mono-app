from typing import List
from fastapi import APIRouter
from .models import Transaction
from .mock_data import MOCK_TRANSACTIONS

# TODO: Find typical FastAPI project structure, watch Arjan, youtube, etc.
router = APIRouter(prefix="/transactions", tags=["transactions"])


@router.get("/", response_model=List[Transaction])
async def get_transactions() -> List[Transaction]:
    return MOCK_TRANSACTIONS
