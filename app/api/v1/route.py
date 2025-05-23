from fastapi import APIRouter
from app.api.v1.controller import Controller
from app.model import OperationalModel, ResultModel

router = APIRouter()
controller=Controller()

# Add two numbers.
@router.post("/add",response_model=ResultModel)
async def add_route(payload: OperationalModel):
    return await controller.add(payload)
# Subtract two numbers.
@router.post("/subtract",response_model=ResultModel)
async def subtract_route(payload: OperationalModel):
    return await controller.subtract(payload)
# Multiply two numbers.
@router.post("/multiply",response_model=ResultModel)
async def multiply_route(payload: OperationalModel):
    return await controller.multiply(payload)
# Divide two numbers.
@router.post("/divide",response_model=ResultModel)
async def divide_route(payload: OperationalModel):
    return await controller.divide(payload)