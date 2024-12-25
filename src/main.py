from fastapi import FastAPI
from transactions.router import router as transactions_router

app = FastAPI(title="Bank Transactions API")

# Include routers
app.include_router(transactions_router)


@app.get("/")
async def root():
    return {"message": "Welcome to Bank Transactions API"}
