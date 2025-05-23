FROM python:3.13-slim

WORKDIR /app

# Install Poetry
RUN pip install poetry==1.8.2

# Copy poetry config files
COPY pyproject.toml poetry.lock* ./

# Configure poetry to not use virtual environments in Docker
RUN poetry config virtualenvs.create false

# Install dependencies
RUN poetry install --no-interaction --no-ansi

# Copy application code
COPY . .

# Expose port
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]