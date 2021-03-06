from sqlalchemy.orm import Session
from hashing import Hash
import models, schemas


def get_user(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.id == user_id)
    return user


def get_users(db: Session):
    return db.query(models.User).all()


def create_user(db: Session, request: schemas.UserCreate):
    hashed_password = Hash.bcrypt(request.password)
    user = models.User(email=request.email, hashed_password=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def delete_user(user_id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    db.delete(user)
    db.commit()
    return user


def update_user(db: Session, request: schemas.UserUpdate, user):
    user.update(request.dict())
    db.commit()


def get_item(db: Session, item_id: int):
    return db.query(models.Item).filter(models.Item.id == item_id)


def get_items(db: Session):
    return db.query(models.Item).all()


def create_item(db: Session, request: schemas.ItemCreate, owner_id: int):
    item = models.Item(**request.dict(), owner_id=owner_id)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def update_item(db: Session, request: schemas.Item, item):
    item.update(request.dict())
    db.commit()


def get_my_items(db: Session, user_id: int):
    print(user_id)
    return db.query(models.Item).filter(models.Item.owner_id == user_id).all()


def delete_item(item, db: Session):
    db.delete(item)
    db.commit()
    return {'deleted'}
