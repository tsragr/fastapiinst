from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
import crud
import database
import schemas
import models

router = APIRouter(
    prefix="/user",
    tags=['Users']
)

get_db = database.get_db


@router.post('/', response_model=schemas.User)
def create_user(request: schemas.UserCreate, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.email).first()
    if user:
        raise HTTPException(status_code=400, detail='Email already registered')
    return crud.create_user(db, request)


@router.get('/', response_model=List[schemas.User])
def get_users(db: Session = Depends(get_db)):
    return crud.get_users(db)


@router.get('/{user_id}/', response_model=schemas.User)
def retrieve_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail='User not Found')
    return user


@router.delete('/{user_id}/')
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return crud.delete_user(user_id, db)


@router.put('/{user_id}/', response_model=schemas.User)
def update_user(request: schemas.UserUpdate, user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if user.first() is None:
        raise HTTPException(status_code=404, detail='User not Found')
    crud.update_user(db, request, user)
    return user.first()
