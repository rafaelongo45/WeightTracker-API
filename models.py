from database import Base
from sqlalchemy import Column, Integer, String

class Exercise(Base):
  __tablename__ = "exercise"
  id = Column(Integer, primary_key = True)
  name = Column(String, unique=True)
  link = Column(String)
  musclegroup = Column(String)

class Users(Base):
  __tablename__ = "users"
  id = Column(Integer, primary_key=True)
  username = Column(String, unique = True)
  email = Column(String, unique=True)
  password = Column(String)