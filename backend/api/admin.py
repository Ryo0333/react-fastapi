from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api import crud, schemas
from api.database import SessionLocal

admin_router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@admin_router.post("/admin", response_model=schemas.User)
def create_admin(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_name(db, name=user.name)
    if db_user:
        raise HTTPException(status_code=400, detail="Name already registered")
    return crud.create_admin(db=db, user=user)
