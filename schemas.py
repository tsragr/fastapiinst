from typing import List, Optional
import datetime
from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None
    time_created: datetime.datetime
    time_updated: datetime.datetime = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(BaseModel):
    email: str
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []
    time_created: datetime.datetime
    time_updated: datetime.datetime = None

    class Config:
        orm_mode = True
