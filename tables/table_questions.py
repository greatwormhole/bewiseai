from sqlalchemy import Column, Integer, Text, DateTime

from ..database import DataBase

class Question(DataBase):
    
    __tablename__ = 'Questions'
    
    question_id = Column(Integer, primary_key=True)
    question_text = Column(Text)
    response_text = Column(Text)
    creation_date = Column(DateTime)
    