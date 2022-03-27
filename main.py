from fastapi import FastAPI
from models import Base
from database import engine
from routing import item, user

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user.router)
app.include_router(item.router)
