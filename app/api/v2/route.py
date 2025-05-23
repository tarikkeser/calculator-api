from fastapi import APIRouter
from app.model import OperationalModel,ResultModel,OperationHistory
from app.api.v2.controller import Controller

from typing import List

router = APIRouter()
controller = Controller()

@router.post("/add", response_model=ResultModel)
async def add_route(payload: OperationalModel):
    return await controller.add(payload)

@router.post("/subtract", response_model=ResultModel)
async def subtract_route(payload: OperationalModel):
    return await controller.subtract(payload)

@router.post("/multiply", response_model=ResultModel)
async def multiply_route(payload: OperationalModel):
    return await controller.multiply(payload)

@router.post("/divide", response_model=ResultModel)
async def divide_route(payload: OperationalModel):
    return await controller.divide(payload)


# Get operation history.
@router.get("/history", response_model=List[OperationHistory])
async def get_history_route():
    return await controller.get_history()