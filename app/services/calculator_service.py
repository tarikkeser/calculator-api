from app.api.v1.models import ResultModel

class CalculatorService:
    # add method to add two numbers.
    @staticmethod
    def add(a: float, b: float) -> float:
        return a + b

    # subtract method to subtract two numbers.
    @staticmethod
    def subtract(a: float, b: float) -> float:
        return a - b
    
    # multiply method to multiply two numbers.
    @staticmethod
    def multiply(a: float, b: float) -> float:
        return a * b
    # divide method to divide two numbers.
    @staticmethod
    def divide(a: float, b: float) -> float:
        if b == 0:
           raise ZeroDivisionError()
        return a / b