import os

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

DOTENV = os.path.join(os.path.dirname(__file__), ".env")


class Settings(BaseSettings):
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    SQLALCHEMY_DATABASE_URL: str = "sqlite:///./sales_info.db"
    SECRET_KEY: str = Field(env="SECRET_KEY")

    model_config = SettingsConfigDict(env_file=DOTENV, env_file_encoding="utf-8")


settings = Settings()
