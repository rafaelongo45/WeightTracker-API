from fastapi import FastAPI, status, HTTPException
from database import Session
from pydantic import BaseModel
import models

class Exercise(BaseModel):
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
  db_exercise = db.query(models.Exercise).filter(models.Exercise.name == exercise.name).first()
  if not db_exercise is None: 
    raise HTTPException(status_code=409, detail="Exercise with this name already exists")
  new_exercise=models.Exercise(
    name=exercise.name,
    link=exercise.link,
    musclegroup=exercise.musclegroup
  )
  db.add(new_exercise)
  db.commit()
  
  return new_exercise
