from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.crud import crud
from api.endpoints.deps import get_db
from core.security import verify_password
from schemas import user

user_router = APIRouter()


@user_router.post("/users", response_model=user.User)
def create_user(user: user.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_name(db, name=user.name)
    if db_user:
        raise HTTPException(status_code=400, detail="Name already registered")

    return crud.create_user(db=db, user=user)


@user_router.get("/users", response_model=user.User)
def read_user(name: str, password: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_name(db=db, name=name)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    if not verify_password(password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Incorrect password")
    return db_user
