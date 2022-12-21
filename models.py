from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey

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
  
class Sessions(Base):
  __tablename__ = "sessions"
  id = Column(Integer, primary_key = True)
  userId = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable = False)
  key = Column(String, nullable = False)