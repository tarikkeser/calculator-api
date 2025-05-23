from app.services.calculator_service import CalculatorService
from app.services.history_service import history_service
from app.model import OperationalModel, ResultModel,OperationHistory
from fastapi import HTTPException
from typing import List

class Controller:
    # Payload = Data that comes to the API and will be processed.
    def __init__(self):
        self.calculator_service = CalculatorService()
        self.history_service = history_service

    async def add(self, payload: OperationalModel) -> ResultModel:
        result = self.calculator_service.add(payload.a, payload.b)
        self.history_service.record_operation("add", payload.a, payload.b, result)
        return ResultModel(result=result)

    async def subtract(self, payload: OperationalModel) -> ResultModel:
        result = self.calculator_service.subtract(payload.a, payload.b)
        self.history_service.record_operation("subtract", payload.a, payload.b, result)
        return ResultModel(result=result)

    async def multiply(self, payload: OperationalModel) -> ResultModel:
        result = self.calculator_service.multiply(payload.a, payload.b)
        self.history_service.record_operation("multiply", payload.a, payload.b, result)
        return ResultModel(result=result)

    async def divide(self, payload: OperationalModel) -> ResultModel:
        try:
            result = self.calculator_service.divide(payload.a, payload.b)
            self.history_service.record_operation("divide", payload.a, payload.b, result)
            return ResultModel(result=result)
        except ZeroDivisionError:
            raise HTTPException(status_code=400, detail="Division by zero is not allowed.")

    async def get_history(self) -> List[OperationHistory]:
        return self.history_service.get_history()
