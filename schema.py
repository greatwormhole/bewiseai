from pydantic import BaseModel

class QuestionPost(BaseModel):
    
    question_num: int
    
    class Config:
        orm_mode = True