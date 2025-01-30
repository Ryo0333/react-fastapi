import os

from pydantic import BaseSettings

DOTENV = os.path.join(os.path.dirname(__file__), ".env")


class Settings(BaseSettings):
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    SQLALCHEMY_DATABASE_URL = "sqlite:///./sales_info.db"

    class Config:
        env_file = DOTENV


settings = Settings()
