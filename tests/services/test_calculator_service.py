import pytest
from app.services.calculator_service import CalculatorService

@pytest.fixture
def calculator_service():
    return CalculatorService()

def test_add(calculator_service):
    result = calculator_service.add(2, 3)
    assert result == 5

def test_subtract(calculator_service):
    result = calculator_service.subtract(5, 3)
    assert result == 2
def test_multiply(calculator_service):
    result = calculator_service.multiply(2, 3)
    assert result == 6
def test_divide(calculator_service):
    result = calculator_service.divide(6, 3)
    assert result == 2
    with pytest.raises(ZeroDivisionError):
        calculator_service.divide(6, 0)