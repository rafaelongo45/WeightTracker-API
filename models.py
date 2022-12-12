from database import Base
from sqlalchemy import Column, Integer, String

class Exercise(Base):
  __tablename__ = "exercise"
  id = Column(Integer, primary_key = True)
  name = Column(String, unique=True)
  link = Column(String)
  musclegroup = Column(String)
  