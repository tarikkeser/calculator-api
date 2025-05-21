from app.services.calculator_service import CalculatorService
from app.api.v1.models import OperationalModel,ResultModel
from fastapi import HTTPException


class Controller:    
 # Payload = Data that comes to the API and will be processed.
    @staticmethod
    async def add(payload: OperationalModel) -> ResultModel:
        result = CalculatorService.add(payload.a, payload.b)
        return ResultModel(result=result)
    @staticmethod
    async def subtract(payload: OperationalModel) -> ResultModel:
        result = CalculatorService.subtract(payload.a, payload.b)
        return ResultModel(result=result)
    @staticmethod
    async def multiply(payload: OperationalModel) -> ResultModel:
        result = CalculatorService.multiply(payload.a, payload.b)
        return ResultModel(result=result)
    @staticmethod
    async def divide(payload: OperationalModel) -> ResultModel:
     try:
        result = CalculatorService.divide(payload.a, payload.b)
        return ResultModel(result=result)
     except ZeroDivisionError:
        raise HTTPException(status_code=400, detail="Division by zero is not allowed.")