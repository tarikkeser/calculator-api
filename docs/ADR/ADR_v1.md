# ADR v1: API Structure and Design Decisions
# Created: 21-07-2025

## Context:
Basic mathematical operations has been implemented in the v1 version of the API.

## Decision:
1. The API has been structured general service class to handle the basic arithmetic operations: addition, subtraction, multiplication, and division.
2. Each version of the API will have its own model, controller and route classes.

## Alternatives Considered:
1. Poetry vs. pip: Poetry was chosen for its dependency management and virtual environment capabilities. Additionally, it simplifies the process of managing dependencies and packaging the application.

## Consequences:
1. Easy to add new API versions or features without breaking existing clients.
2. Clear separation of concerns, making the codebase easier to maintain and extend.