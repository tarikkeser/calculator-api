# Calculator API
A simple versioned REST API built with Python, FastAPI, Poetry.
This API provides basic arithmetic operations such as addition, subtraction, multiplication, and division. It also includes a versioning system to manage different versions of the API.

## Features
- Basic arithmetic operations: addition, subtraction, multiplication, and division.
- API versioning.
- Automatic API documentation with Swagger UI. Access it at `http://localhost:8000/docs`.

## Folder Structure 
- app/         : Main application code (API, services, core config)
- tests/       : Unit and integration tests
- docs/        : Project documentation (e.g., ADRs)
- README.md    : Project overview and usage instructions
- pyproject.toml : Project dependencies and configuration


## API Endpoints - v1
| Method | Path             | Description              |
|--------|------------------|--------------------------|
| POST   | /api/v1/add      | Adds two numbers         |
| POST   | /api/v1/subtract | Subtracts two numbers    |
| POST   | /api/v1/multiply | Multiplies two numbers   |
| POST   | /api/v1/divide   | Divides two numbers      |


## Installation 

1. Install dependencies:
    ```bash
    poetry install
    ```
2. Run the application:
    ```bash
    poetry run uvicorn app.main:app --reload
    ```



