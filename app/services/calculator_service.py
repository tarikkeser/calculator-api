class CalculatorService:
    
    # self = this in C#
    
    # add method to add two numbers.

    def add(self,a: float, b: float) -> float:
        return a + b

    # subtract method to subtract two numbers.

    def subtract(self,a: float, b: float) -> float:
        return a - b
    
    # multiply method to multiply two numbers.

    def multiply(self,a: float, b: float) -> float:
        return a * b
    # divide method to divide two numbers.

    def divide(self,a: float, b: float) -> float:
        if b == 0:
           raise ZeroDivisionError()
        return a / b