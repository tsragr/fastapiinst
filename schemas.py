from typing import List, Optional
import datetime
from pydantic import BaseModel


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


class Item(ItemBase):
    id: int
    owner: UserBase
    time_created: datetime.datetime
    time_updated: datetime.datetime = None

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    pass


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []
    time_created: datetime.datetime
    time_updated: datetime.datetime = None

    class Config:
        orm_mode = True
