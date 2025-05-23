from app.services.calculator_service import CalculatorService
from app.model import OperationalModel,ResultModel
from fastapi import HTTPException


class Controller:    
 # Payload = Data that comes to the API and will be processed.
 def __init__(self):
     self.calculator_service = CalculatorService()
     
 async def add(self,payload: OperationalModel) -> ResultModel:
        result = self.calculator_service.add(payload.a, payload.b)
        return ResultModel(result=result)

 async def subtract(self,payload: OperationalModel) -> ResultModel:
        result = self.calculator_service.subtract(payload.a, payload.b)
        return ResultModel(result=result)

 async def multiply(self,payload: OperationalModel) -> ResultModel:
        result = self.calculator_service.multiply(payload.a, payload.b)
        return ResultModel(result=result)

 async def divide(self,payload: OperationalModel) -> ResultModel:
      try:
        result = self.calculator_service.divide(payload.a, payload.b)
        return ResultModel(result=result)
      except ZeroDivisionError:
        raise HTTPException(status_code=400, detail="Division by zero is not allowed.")