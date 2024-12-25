import uvicorn


def start_server() -> None:
    """Start the FastAPI server with specified configuration"""
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, log_level="info")


if __name__ == "__main__":
    start_server()
