from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api import crud, schemas
from api.database import SessionLocal

user_router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@user_router.post("/users", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_name(db, name=user.name)
    if db_user:
        raise HTTPException(status_code=400, detail="Name already registered")

    return crud.create_user(db=db, user=user)


@user_router.get("/users", response_model=schemas.User)
def read_user(name: str, password: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_name_by_password(db, name=name, password=password)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
