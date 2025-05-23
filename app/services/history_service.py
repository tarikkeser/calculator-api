from typing import List
from datetime import datetime
from app.model import OperationHistory

class HistoryService:
    
    def __init__(self):
        self.history: List[OperationHistory] = []

    def record_operation(self, operation: str, a: float, b: float, result: float):
        operation_history = OperationHistory(
            timestamp=datetime.now(),
            operation=operation,
            a=a,
            b=b,
            result=result
        )
        self.history.append(operation_history)

    def get_history(self) -> List[OperationHistory]:
        return self.history
    
    def clear_history(self):
        self.history.clear()
        
# Singletoon instance        
history_service = HistoryService()        
    
    