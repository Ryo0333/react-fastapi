from sqlalchemy.orm import Session

from models.sales import SalesTable
from schemas.sales import Sales, SalesCreate, SalesUpdate


def get_sales(db: Session):
    return db.query(SalesTable).all()


def get_sales_by_year(db: Session, year: int):
    return db.query(SalesTable).filter(Sales.year == year).all()


def get_sales_by_year_by_department(db: Session, year: int, department: str):
    return (
        db.query(SalesTable)
        .filter(Sales.year == year)
        .filter(Sales.department == department)
        .first()
    )


def create_sales(db: Session, sales: SalesCreate):
    db_sales = Sales(year=sales.year, department=sales.department, sales=sales.sales)
    db.add(db_sales)
    db.commit()
    db.refresh(db_sales)
    return db_sales


def update_sales(db: Session, sales: SalesUpdate):
    db_sales = get_sales_by_year_by_department(
        db, year=sales.year, department=sales.department
    )
    db_sales.sales = sales.sales
    db.commit()
    db.refresh(db_sales)
    return db_sales
