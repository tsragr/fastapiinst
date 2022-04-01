from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud
import database
import models
import schemas
import oauth2

router = APIRouter(
    prefix="/item",
    tags=['Items']
)

get_db = database.get_db


@router.post('/', response_model=schemas.Item)
def create_item(request: schemas.ItemCreate, db: Session = Depends(get_db),
                current_user: schemas.User = Depends(oauth2.get_current_user)):
    return crud.create_item(db, request, current_user.id)


@router.get('/', response_model=List[schemas.Item])
def get_items(db: Session = Depends(get_db)):
    return crud.get_items(db)


@router.get('/my_items/', response_model=List[schemas.MyItem])
def get_my_items(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return crud.get_my_items(db, current_user.id)


@router.get('/{item_id}/', response_model=schemas.Item)
def get_item(item_id: int, db: Session = Depends(get_db),
             current_user: schemas.User = Depends(oauth2.get_current_user)):
    item = crud.get_item(db, item_id)
    if item.first() is None:
        raise HTTPException(status_code=404, detail='Item not Found')
    return item.first()


@router.put('/{item_id}/', response_model=schemas.Item)
def update_user(request: schemas.ItemUpdate, item_id: int, db: Session = Depends(get_db),
                current_user: schemas.User = Depends(oauth2.get_current_user)):
    item = crud.get_item(db, item_id)
    if item.first() is None:
        raise HTTPException(status_code=404, detail='Item not Found')
    if item.first().owner_id != current_user.id:
        raise HTTPException(status_code=400, detail='Permission denied')
    crud.update_item(db, request, item)
    return item.first()


@router.delete('/{item_id}')
def delete_item(item_id: int, db: Session = Depends(get_db),
                current_user: schemas.User = Depends(oauth2.get_current_user)):
    item = crud.get_item(db, item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail='Item not Found')
    if item.owner_id != current_user.id:
        raise HTTPException(status_code=400, detail='Permission denied')
    return crud.delete_item(item, db)
