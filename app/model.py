from pydantic import BaseModel
from datetime import datetime


# v1 
class OperationalModel(BaseModel):
    a: float
    b: float
# v1
class ResultModel(BaseModel):
    result: float
    
# v2
class OperationHistory(BaseModel):
    timestamp: datetime
    operation: str
    a: float
    b: float
    result: float