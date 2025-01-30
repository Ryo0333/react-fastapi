from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.crud import users
from api.endpoints.deps import get_db
from core.security import verify_password
from schemas.user import UserCreate, UserInDB

user_router = APIRouter()


@user_router.post("/users", response_model=UserInDB)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = users.get_user_by_name(db, name=user.name)
    if db_user:
        raise HTTPException(status_code=400, detail="Name already registered")

    return users.create_user(db=db, user=user)


@user_router.get("/users", response_model=UserInDB)
def read_user(name: str, password: str, db: Session = Depends(get_db)):
    db_user = users.get_user_by_name(db=db, name=name)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    if not verify_password(password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Incorrect password")
    return db_user
