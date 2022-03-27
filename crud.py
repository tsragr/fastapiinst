from sqlalchemy.orm import Session

import models, schemas


def get_user(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    return user


def get_users(db: Session):
    return db.query(models.User).all()


def create_user(db: Session, request: schemas.UserCreate):
    fake_hashed_password = '123qweewq312'
    print(request.dict())
    user = models.User(email=request.email, hashed_password=fake_hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def delete_user(user_id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    db.delete(user)
    db.commit()
    return {'result': 'success'}


def get_item(db: Session, item_id: int):
    return db.query(models.Item).filter(models.User.id == item_id).first()


def get_items(db: Session):
    return db.query(models.Item).all()


def create_item(db: Session, request: schemas.ItemCreate, owner_id: int):
    item = models.Item(**request.dict(), owner_id=owner_id)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item
