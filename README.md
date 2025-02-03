# Mono App

A FastAPI-based application that provides financial data through REST API endpoints.

## Prerequisites

- Homebrew (for installing tools on macOS)
- Python 3.13 (installed via pyenv)
- uv package installer (`brew install uv`)
- pre-commit (`brew install pre-commit`)

## Installation

1. Install Python 3.13 using pyenv:
```bash
# Install pyenv if you haven't already
brew install pyenv

# Install Python 3.13.1
pyenv install 3.13.1
pyenv local 3.13.1
```

2. Create and activate a virtual environment:
```bash
# Create virtual environment using uv
uv venv --python 3.13

# Activate it
source .venv/bin/activate
```

3. Install all dependencies (including development):
```bash
# Install all dependencies at once
uv sync
```

4. Set up pre-commit hooks:
```bash
# Install the git hooks
brew install pre-commit
pre-commit install
```

## Running the Application

1. Start the FastAPI server:
```bash
uvicorn src.api:app --reload --host 0.0.0.0 --port 8000
```

The `--host 0.0.0.0` flag makes the server accessible from any network interface, and `--port 8000` explicitly sets the port. You should see output like:
```
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Application startup complete.
```

2. The API will be available at:
   - Local access: http://localhost:8000
   - Network access: http://<your-ip-address>:8000

To stop the server, press CTRL+C in the terminal.

## Available Endpoints

- GET `/accounts` - Returns a list of mock accounts
- GET `/categories` - Returns a list of mock categories
- GET `/transactions` - Returns a list of mock transactions

## API Documentation

Once the server is running, you can access:
- Interactive API documentation (Swagger UI) at http://localhost:8000/docs
- Alternative API documentation (ReDoc) at http://localhost:8000/redoc

## Development

This project uses:
- FastAPI for the web framework
- Pydantic for data modeling
- Polyfactory for generating mock data
- Ruff for linting
- Pyright for type checking
- Pytest for testing

### Development Tools Setup

Install development tools:
```bash
# Install Node.js (required for pyright)
brew install node

# Install pyright globally
npm install -g pyright

# Install ruff
brew install ruff
```

### Running Development Tools

Make sure your virtual environment is activated:
```bash
source .venv/bin/activate
```

To run tests with coverage:
```bash
python -m pytest --cov=src tests/
```

To run type checking:
```bash
pyright
```

To run linting:
```bash
ruff check .
```