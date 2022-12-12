from database import Base, engine
from models import Exercise

print("Creating database...")

Base.metadata.create_all(engine)



