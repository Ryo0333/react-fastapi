from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.crud import sales as sales_crud
from api.endpoints.deps import get_db
from schemas.sales import Sales

sales_router = APIRouter()


@sales_router.get("/sales", response_model=list[Sales])
def read_sales(db: Session = Depends(get_db)):
    sales = sales_crud.get_sales(db)
    if sales is None:
        raise HTTPException(status_code=404, detail="Sales Info not found")
    return sales


@sales_router.get("/sales/{year}", response_model=list[Sales])
def read_sales_by_year(year: int, db: Session = Depends(get_db)):
    sales = sales_crud.get_sales_by_year(db, year=year)
    return sales
