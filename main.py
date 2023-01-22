from fastapi.security import OAuth2PasswordBearer
from routing import item, user, authenticate
from fastapi import FastAPI
from models import Base
from database import engine

app = FastAPI()

# Base.metadata.create_all(bind=engine)

app.include_router(authenticate.router)
app.include_router(user.router)
app.include_router(item.router)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
