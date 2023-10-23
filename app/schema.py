from pydantic import BaseModel
from datetime import datetime

class QuestionPOSTRequestData(BaseModel):
    
    questions_num: int
    
    class Config:
        orm_mode = True
        
class QuestionPOSTResponseData(BaseModel):
    id: int
    answer: str
    question: str
    created_at: datetime
    updated_at: datetime
    airdate: datetime
    value: int
    category_id: int
    game_id: int
    invalid_count: int
    