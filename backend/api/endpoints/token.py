from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from api.endpoints.deps import get_db
from core.config import settings
from core.security import (
    authenticate_user,
    create_access_token,
)
from schemas.token import Token

token_router = APIRouter()


@token_router.post("/token")
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
) -> Token:
    user = authenticate_user(
        name=form_data.username, password=form_data.password, db=db
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.name, "role": user.role},
        expires_delta=access_token_expires,
    )
    return Token(access_token=access_token, token_type="bearer")
