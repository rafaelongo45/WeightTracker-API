from fastapi import FastAPI, status
from database import Session
from pydantic import BaseModel
import models

class Exercise(BaseModel):
  id: int
  name: str
  link: str
  musclegroup: str

app = FastAPI()
db = Session()

@app.get("/exercises", status_code=200)
def get_exercises(): 
  items = db.query(models.Exercise).all()
  return items

@app.post("/exercises", status_code=status.HTTP_201_CREATED)
def post_exercise(exercise: Exercise):
  new_exercise=models.Exercise(
    id=exercise.id,
    name=exercise.name,
    link=exercise.link,
    musclegroup=exercise.musclegroup
  )
  db.add(new_exercise)
  db.commit()
  
  return new_exercise
