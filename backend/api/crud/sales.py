from sqlalchemy.orm import Session

from models.sales import SalesTable
from schemas.sales import SalesCreate, SalesUpdate


def get_sales(db: Session):
    return db.query(SalesTable).all()


def get_sales_by_year(db: Session, year: int):
    return db.query(SalesTable).filter(SalesTable.year == year).all()


def get_sales_by_year_by_department(db: Session, year: int, department: str):
    return (
        db.query(SalesTable)
        .filter(SalesTable.year == year)
        .filter(SalesTable.department == department)
        .first()
    )


def create_sales(db: Session, sales: SalesCreate):
    db_sales = SalesTable(
        year=sales.year, department=sales.department, sales=sales.sales
    )
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
