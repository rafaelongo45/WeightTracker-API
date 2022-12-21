import models

from database import Session
from pydantic import BaseModel
from fastapi import FastAPI, status, HTTPException
from utils.password_hasher import hash_password, verify_password
from utils.auth_handler import sign_jwt, decodeJWT

class Exercise(BaseModel):
  name: str
  link: str
  musclegroup: str

class User(BaseModel):
  username: str
  email: str
  password: str

class SigninUser(BaseModel):
  email: str
  password: str

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

@app.post("/signup", status_code=201)
def signup(user: User):
  db_email = db.query(models.Users).filter(models.Users.email == user.email).first()
  db_user = db.query(models.Users).filter(models.Users.username == user.username).first()
  if not db_email == None:
    raise HTTPException(status_code=409, detail="User with this email was already created")
  if not db_user == None:
    raise HTTPException(status_code=409, detail="User with this username was already registered")
  
  hashed_password = hash_password(user.password)
  
  new_user=models.Users(
    username=user.username,
    email=user.email,
    password=hashed_password
  )
  db.add(new_user)
  db.commit()
  return "Ok"

@app.post("/signin", status_code=200)
def signin(user:SigninUser):
  db_email = db.query(models.Users).filter(models.Users.email == user.email).first()
  if db_email == None:
    raise HTTPException(status_code=404, detail="Couldn't find a user registered with this email")
  is_password_correct = verify_password(user.password, db_email.password)
  if is_password_correct == False:
    raise HTTPException(status_code=403, detail="Incorrect password")
  user_id = db_email.id
  token = sign_jwt(user_id)
  session = models.Sessions(
    userId = user_id,
    key = token["access_token"]
  )
  db.add(session)
  db.commit()
  return token

#TODO: Create folder structure