from fastapi import FastAPI
from transactions.router import router as transactions_router

# TODO: fix mypy imports
# TODO: Configure ruff and on commit, what is different from black?
# TODO: Figure out what is JsonSchema
# TODO: Add logging
# TODO: How to hide unnecesary folders in vscode?


app = FastAPI()
app.include_router(transactions_router)


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Welcome to Bank Transactions API"}
