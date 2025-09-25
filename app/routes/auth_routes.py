from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.utils.jwt_handler import verify_token
from app.database import get_db

oauth2_scheme = OAuth2PasswordBearer  (tokenUrl="/auth/login")

async def get_current_user(token: str = Depends(oauth2_scheme)):
  payload = verify_token(token)
  if not payload:
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

  return payload