from pydantic import BaseModel

class OperationalModel(BaseModel):
    a: float
    b: float

class ResultModel(BaseModel):
    result: float