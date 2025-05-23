# Solution Approach for the assignment.
1- Explore FAST API and understand the basic concepts by watching comparison tutorials.
2- Learn the essential folder structure of a FastAPI project and how to set it up.
3- Learn the packet management system Poetry and how to use it for managing dependencies in a FastAPI project. Additionally, compare it with pip.
4- Learn the versioning of APIs and how to implement it in FastAPI.

# Usage of AI in the project.
1- Comparison of Python classes and functions with C# by using ChatGPT.
2- Understanding the basic concepts of FastAPI and how to set up a project structure with the help of ChatGPT.
3- Understanding the basic concepts of Poetry and how to set up a project structure with the help of Github Copilot.
4- Understanding the containerization (Docker and Docker Compose) of the FastAPI project with the help of Github Copilot and ChatGPT.

# Calculator API
A simple versioned REST API built with Python, FastAPI, Poetry.
This API provides basic arithmetic operations such as addition, subtraction, multiplication, and division. It also includes a versioning system to manage different versions of the API.

## Features
- Basic arithmetic operations: addition, subtraction, multiplication, and division and history of operations.
- API versioning.
- Automatic API documentation with Swagger UI. Access it at `http://localhost:8000/docs`.
- Tests for all endpoints and services.
- Containerization with Docker for easy deployment and scalability.

## Folder Structure 
- app/         : Main application code (API, services, core config)
- tests/       : Unit and integration tests
- docs/        : Project documentation (e.g., ADRs)
- README.md    : Project overview and usage instructions
- pyproject.toml : Project dependencies and configuration
- Dockerfile   : Dockerfile for containerization
- docker-compose.yml : Docker Compose file for multi-container setup


## Installation and Run

1. Clone the repository:
```bash
docker-compose up
```
2. Go to http://localhost:8000/docs to see the Swagger UI API documentation.


## Future Improvements
-  Complex mathematical operations (e.g., exponentiation, square root, etc.).
-  Better error handling and validation.
-  Error logging.
-  UI integration for the API. (for example , a front end framework like Vue.js)