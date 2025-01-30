from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.crud import admin
from api.endpoints.deps import get_db
from schemas.user import User, UserCreate

admin_router = APIRouter()


@admin_router.post("/admin", response_model=User)
def create_admin(user: UserCreate, db: Session = Depends(get_db)):
    db_user = admin.get_admin_by_name(db, name=user.name)
    if db_user:
        raise HTTPException(status_code=400, detail="Name already registered")
    return admin.create_admin(db=db, user=user)
