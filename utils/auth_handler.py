import jwt
import time

from typing import Dict
from decouple import config

JWT_SECRET = config("JWT_KEY")
ALGORITHM = config("ALGORITHM")

def token_response(token: str):
  return {
    'access_token': token
  }

def sign_jwt(user_id: int) -> Dict[int, int]:
  payload = {
    "user_id": user_id,
    "time": time.time() + 3600 * 4
  }
  
  token = jwt.encode(payload, JWT_SECRET, algorithm = ALGORITHM)
  return token_response(token)

def decodeJWT(token: str) -> dict:
  try:
    decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[ALGORITHM])
    if decoded_token["expires"] >= time.time():
      return decoded_token
    else:
      return None
  except:
    return {}