from fastapi import APIRouter
from app.api.v1.controllers import Controller
from app.api.v1.models import OperationalModel, ResultModel

router = APIRouter()

# Add two numbers.
@router.post("/add",response_model=ResultModel)
async def add_route(payload: OperationalModel):
    return await Controller.add(payload)
# Subtract two numbers.
@router.post("/subtract",response_model=ResultModel)
async def subtract_route(payload: OperationalModel):
    return await Controller.subtract(payload)
# Multiply two numbers.
@router.post("/multiply",response_model=ResultModel)
async def multiply_route(payload: OperationalModel):
    return await Controller.multiply(payload)
# Divide two numbers.
@router.post("/divide",response_model=ResultModel)
async def divide_route(payload: OperationalModel):
    return await Controller.divide(payload)