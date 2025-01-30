from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.crud import crud
from api.endpoints.deps import get_db
from schemas import user

admin_router = APIRouter()


@admin_router.post("/admin", response_model=user.User)
def create_admin(user: user.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_name(db, name=user.name)
    if db_user:
        raise HTTPException(status_code=400, detail="Name already registered")
    return crud.create_admin(db=db, user=user)
