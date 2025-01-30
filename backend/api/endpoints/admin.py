from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.crud import admin
from api.endpoints.deps import get_db
from core.security import verify_password
from schemas.user import UserCreate, UserInDB

admin_router = APIRouter()


@admin_router.post("/admin", response_model=UserInDB)
def create_admin(user: UserCreate, db: Session = Depends(get_db)):
    db_user = admin.get_admin_by_name(db, name=user.name)
    if db_user:
        raise HTTPException(status_code=400, detail="Name already registered")
    return admin.create_admin(db=db, user=user)


@admin_router.get("/admin", response_model=UserInDB)
def read_admin(name: str, password: str, db: Session = Depends(get_db)):
    db_user = admin.get_admin_by_name(db, name=name)
    if db_user:
        raise HTTPException(status_code=400, detail="Name already registered")
    if not verify_password(password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Incorrect password")
    return admin.get_admin(db=db, name=name)
