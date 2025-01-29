from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api import crud, schemas
from api.database import SessionLocal

sales_router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@sales_router.post("/admin/sales", response_model=schemas.Sales)
def create_sales(name: str, sales: schemas.SalesCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_name(db, name=name)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    if db_user.role != "admin":
        raise HTTPException(status_code=403, detail="User is not admin")
    db_sales = crud.get_sales_by_year_by_department(
        db, year=sales.year, department=sales.department
    )
    if db_sales:
        raise HTTPException(status_code=400, detail="Sales Info already registerd")
    return crud.create_sales(db=db, sales=sales)


@sales_router.put("/admin/sales", response_model=schemas.Sales)
def update_sales(name: str, sales: schemas.SalesUpdate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_name(db, name=name)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    if db_user.role != "admin":
        raise HTTPException(status_code=403, detail="User is not admin")
    db_sales = crud.get_sales_by_year_by_department(
        db, year=sales.year, department=sales.department
    )
    if db_sales is None:
        raise HTTPException(status_code=404, detail="Sales Info not found")
    return crud.update_sales(db=db, sales=sales)


@sales_router.get("/sales", response_model=list[schemas.Sales])
def read_sales(db: Session = Depends(get_db)):
    sales = crud.get_sales(db)
    return sales


@sales_router.get("/sales/{year}", response_model=list[schemas.Sales])
def read_sales_by_year(year: int, db: Session = Depends(get_db)):
    sales = crud.get_sales_by_year(db, year=year)
    return sales
