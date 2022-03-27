from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()
postgres_db = os.getenv('POSTGRES_DB')
postgres_user = os.getenv('POSTGRES_USER')
postgres_password = os.getenv('POSTGRES_PASSWORD')
postgres_host = os.getenv('POSTGRES_HOST')
postgres_port = os.getenv('POSTGRES_PORT')

SQLALCHEMY_DATABASE_URL = f'postgresql://{postgres_user}:{postgres_password}@{postgres_host}:{postgres_port}/' \
                          f'{postgres_db}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3cd5876... init commit

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
<<<<<<< HEAD
        db.close()
=======
>>>>>>> 9204f15... init commit
=======
        db.close()
>>>>>>> 3cd5876... init commit
