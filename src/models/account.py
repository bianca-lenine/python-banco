from database import Base
from sqlalchemy import Column, Integer, String


class Account(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)
