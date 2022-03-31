from routing import item, user
from fastapi import FastAPI
from models import Base
from database import engine

app = FastAPI()

Base.metadata.create_all(bind=engine)


app.include_router(user.router)
app.include_router(item.router)
