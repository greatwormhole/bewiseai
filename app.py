from fastapi import Depends
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

from .database import get_db
from .conf import app
from .schema import QuestionPost

@app.post('/', response_model=QuestionPost)
async def post_new_question(amount: int, db: Session = Depends(get_db)):
    return JSONResponse(
        
    )
