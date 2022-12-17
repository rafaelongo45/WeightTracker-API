import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

load_dotenv()
DATABASE_URI=os.getenv("DATABASE_URI")

engine = create_engine(DATABASE_URI, echo = True)

Base = declarative_base()
Session = sessionmaker(bind=engine)