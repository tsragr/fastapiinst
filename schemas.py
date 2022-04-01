from typing import List, Optional
import datetime
from pydantic import BaseModel
from fastapi.param_functions import Form, File


class UserBase(BaseModel):
    email: str

    class Config:
        orm_mode = True


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


class ItemUpdate(ItemBase):
    pass


class ItemCreate(ItemBase):
    pass


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None
    time_created: datetime.datetime
    time_updated: datetime.datetime = None


class MyItem(ItemBase):
    id: int

    class Config:
        orm_mode = True


class Item(ItemBase):
    id: int

    owner: UserBase

    class Config:
        orm_mode = True


class UserUpdate(UserBase):
    pass


class UserBase(BaseModel):
    email: str


class UserCreate(BaseModel):
    email: str = Form(...)
    password: str = Form(...)


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []
    time_created: datetime.datetime
    time_updated: datetime.datetime = None

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str
