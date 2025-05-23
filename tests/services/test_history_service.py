from app.services.history_service import HistoryService
from app.model import OperationHistory

def test_record_operation():
    service = HistoryService()
    
    assert service.get_history() == []
    
    service.record_operation("add", 1, 2, 3)
    service.record_operation("subtract", 5, 3, 2)
    
    history = service.get_history()
    assert len(history) == 2
    
    assert history[0].operation == "add"
    assert history[0].a == 1
    assert history[0].b == 2
    assert history[0].result == 3
    
    
    assert history[1].operation == "subtract"
    assert history[1].a == 5
    assert history[1].b == 3
    assert history[1].result == 2
    
    