from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
import json

from database.database import get_db
from .schema import QuestionPOSTRequestData
from .service import get_random_posts, update_db
from database.tables.table_questions import Question

app = FastAPI()

@app.post('/')
async def post_new_question(question_info: QuestionPOSTRequestData, db: Session = Depends(get_db)):
    posts = await get_random_posts(question_info.questions_num)
    for post in json.loads(posts):
        print(post)
        update_db(db, post)
    print(db.query(Question).all())