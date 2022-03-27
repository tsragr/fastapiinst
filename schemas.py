from typing import List, Optional
import datetime
from pydantic import BaseModel


<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3cd5876... init commit
class UserBase(BaseModel):
    email: str

    class Config:
        orm_mode = True


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


class ItemUpdate(ItemBase):
    pass
<<<<<<< HEAD
=======
class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None
    time_created: datetime.datetime
    time_updated: datetime.datetime = None
>>>>>>> 9204f15... init commit
=======
>>>>>>> 3cd5876... init commit


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
<<<<<<< HEAD
<<<<<<< HEAD
    owner: UserBase
    time_created: datetime.datetime
    time_updated: datetime.datetime = None
=======
    owner_id: int
>>>>>>> 9204f15... init commit
=======
    owner: UserBase
    time_created: datetime.datetime
    time_updated: datetime.datetime = None
>>>>>>> 3cd5876... init commit

    class Config:
        orm_mode = True


<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3cd5876... init commit
class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    pass
<<<<<<< HEAD
=======
class UserBase(BaseModel):
    email: str


class UserCreate(BaseModel):
    email: str
    password: str
>>>>>>> 9204f15... init commit
=======
>>>>>>> 3cd5876... init commit


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []
    time_created: datetime.datetime
    time_updated: datetime.datetime = None

    class Config:
        orm_mode = True
