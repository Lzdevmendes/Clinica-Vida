from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.user import User
from app.utils.security import hash_password, verify_password
from app.utils.jwt_handler import create_access_token

class AuthService:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, email: str, password: str, role: str) -> User:
        if self.db.query(User).filter(User.email == email).first():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )

        hashed_pwd = hash_password(password)
        user = User(
            email=email,
            hashed_password=hashed_pwd,
            role=role
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def authenticate_user(self, email: str, password: str) -> str:
        user = self.db.query(User).filter(User.email == email).first()
        if not user or not verify_password(password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials"
            )

        if not user.is_active:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User account is inactive"
            )

        access_token = create_access_token(
            data={"sub": user.email, "user_id": user.id, "role": user.role}
        )
        return access_token

    def get_user_by_email(self, email: str) -> User:
        return self.db.query(User).filter(User.email == email).first()