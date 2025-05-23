# ADR v2: API Structure,Design Decisions,Additional Features
# Created: 23-07-2025

## Context:
The patterns and practices fully converted to OOP, with the addition of a history feature to track previous calculations. The API is built with Python, FastAPI, and Poetry.

The project structure has been updated. Single model class have been created for each version of the API.


## Decision:
1. The base model class have been created instead of creating a separate model class for each version of the API.
2. Docker containerization has been added to the project for easy deployment and scalability.
3. History feature used Singleton pattern to store the history of calculations.

## Alternatives Considered:
1- Single pattern for history feature: The Singleton pattern was chosen to ensure that there is only one instance of the history class throughout the application. This allows for easy access and management of the calculation history without creating multiple instances.

## Consequences:
1. The API is now fully OOP-based, making it easier to maintain and extend in the future.
2. The history feature allows users to track their previous calculations, enhancing the user experience.
3. The project is now containerized, making it easier to deploy and scale in different environments.
4. The project structure is more organized, with a clear separation of concerns between different components of the application.


