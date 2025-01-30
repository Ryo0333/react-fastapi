from datetime import datetime, timedelta, timezone
from typing import Union

from fastapi import APIRouter, Depends
from jose import jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from api.crud.users import get_user_by_name
from api.endpoints.deps import get_db
from core.config import settings

token_router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def authenticate_user(name: str, password: str, db: Session = Depends(get_db)):
    user = get_user_by_name(db, name)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM
    )
    return encoded_jwt
