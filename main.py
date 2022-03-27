from typing import Optional, List
from pydantic import BaseModel
from fastapi import FastAPI, Depends, HTTPException
import datetime
import crud, models
from models import Base
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from schemas import UserCreate, User

app = FastAPI()

Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/user/', response_model=User)
def create_user(request: UserCreate, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.email).first()
    if user:
        raise HTTPException(status_code=400, detail='Email already registered')
    return crud.create_user(db, request)


@app.get('/user/', response_model=List[User])
def get_users(db: Session = Depends(get_db)):
    return crud.get_users(db)


@app.get('/user/{user_id}', response_model=User)
def retrieve_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail='User not Found')
    return user


@app.delete('/user/{user_id}')
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return crud.delete_user(user_id, db)
