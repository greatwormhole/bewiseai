from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

DATABASE_URL = 'postgresql+psycopg2://postgres:adminqwerty@postgres:5432/bewiseDB'

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

DataBase = declarative_base()

def get_db():
    with SessionLocal() as db:
        return db