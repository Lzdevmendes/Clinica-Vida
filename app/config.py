from pydantic_settings import BaseSettings
class Settings(BaseSettings):
  DATABASE_URL: str
  SECRET_KEY: str
  ALGORITHM: str = "HS256"
  ACESS_TOKEN_EXPIRE_MINUTES: int = 30
  MAIL_USERNAME: str | None = None
  MAIL_PASSWORD: str | None = None

class Config:
  env_file = ".env"
  
settings = Settings()
