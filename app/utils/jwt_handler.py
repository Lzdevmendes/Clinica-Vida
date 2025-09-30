from datetime import datetime, timedelta
from jose import jwt, JWTError
from app.config import settings

def create_access_token(data: dict, expires_minutes: int | None = None):
  to_encode = data.copy()
  expire = datetime.utcnow() + timedelta(minutes=expires_minutes or settings.ACCESS_TOKEN_EXPIRE_MINUTES)
  to_encode.update({"exp": expire})
  encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
  return encoded_jwt

def verify_token(token: str):
  try:
    payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    return payload
  except JWTError:
    return None
  