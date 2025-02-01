from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.crud import admin
from api.crud import sales as sales_crud
from api.endpoints.deps import get_current_admin_user, get_db
from core.security import verify_password
from schemas.sales import Sales, SalesCreate, SalesUpdate
from schemas.user import UserCreate, UserInDB

admin_router = APIRouter(dependencies=[Depends(get_current_admin_user)])


@admin_router.post("/admin", response_model=UserInDB)
def create_admin(user: UserCreate, db: Session = Depends(get_db)):
    db_user = admin.get_admin_by_name(db, name=user.name)
    if db_user:
        raise HTTPException(status_code=400, detail="Name already registered")
    return admin.create_admin(db=db, user=user)


@admin_router.get("/admin", response_model=UserInDB)
def read_admin(name: str, password: str, db: Session = Depends(get_db)):
    db_user = admin.get_admin_by_name(db, name=name)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    if not verify_password(password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Incorrect password")
    return admin.get_admin(db, name=name)


@admin_router.post("/admin/sales", response_model=Sales)
def create_sales(name: str, sales: SalesCreate, db: Session = Depends(get_db)):
    db_user = admin.get_admin_by_name(db, name=name)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_sales = sales_crud.get_sales_by_year_by_department(
        db, year=sales.year, department=sales.department
    )
    if db_sales:
        raise HTTPException(status_code=400, detail="Sales Info already registerd")
    return sales_crud.create_sales(db=db, sales=sales)


@admin_router.put("/admin/sales", response_model=Sales)
def update_sales(name: str, sales: SalesUpdate, db: Session = Depends(get_db)):
    db_user = admin.get_admin_by_name(db, name=name)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_sales = sales_crud.get_sales_by_year_by_department(
        db, year=sales.year, department=sales.department
    )
    if db_sales is None:
        raise HTTPException(status_code=404, detail="Sales Info not found")
    return sales_crud.update_sales(db=db, sales=sales)
