import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv

load_dotenv()

database_url = os.environ.get('SQLALCHEMY_DATABASE_URL') or "sqlite:///./database.db"
engine = create_engine(database_url, connect_args={'check_same_thread': False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
