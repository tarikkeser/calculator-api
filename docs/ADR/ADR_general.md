# ADR v1: API Structure and Design Decisions
# Created: 21-07-2025

## Context:
The project is a simple versioned REST API built with Python, FastAPI, and Poetry.

## Decision:
1. The API will be structured to support versioning, allowing for future enhancements and backward compatibility.
2. The API will provide basic arithmetic operations: addition, subtraction, multiplication, division and history of calculations.
3. The API will use FastAPI for its asynchronous capabilities and automatic generation of OpenAPI documentation.
4. OOP principles will be applied to the codebase, ensuring that the code is modular and easy to maintain.
5. Docker containerization will be used for easy deployment and scalability.

## Alternatives Considered:
1. Poetry vs. pip: Poetry was chosen for its dependency management and virtual environment capabilities. Additionally, it simplifies the process of managing dependencies and packaging the application.

## Consequences:
1. Easy to add new API versions or features without breaking existing clients.
2. Clear separation of concerns, making the codebase easier to maintain and extend.