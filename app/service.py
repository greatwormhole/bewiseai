import aiohttp
from sqlalchemy.orm import Session

from .conf import URL_PATH
from .schema import QuestionPOSTResponseData
from database.tables.table_questions import Question

async def get_random_posts(amount: int):
    
    relative_path = '/api/random'
    kwargs = f'?count={amount}'
    URI = URL_PATH + relative_path + kwargs # temp
    
    async with aiohttp.ClientSession() as session:
        async with session.get(URI) as resp:
            return await resp.text()
        
def update_db(db: Session, question: dict):
    db_question = Question(
        id=question['id'],
        question_text=question['question'],
        response_text=question['answer'],
        created_at=question['created_at']
    )
    db.add(db_question)
    db.commit()
    db.refresh()
    
    return db_question