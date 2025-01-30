import os

from pydantic_settings import BaseSettings

DOTENV = os.path.join(os.path.dirname(__file__), ".env")


class Settings(BaseSettings):
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    SQLALCHEMY_DATABASE_URL: str = "sqlite:///./sales_info.db"

    class Config:
        env_file = DOTENV


settings = Settings()
