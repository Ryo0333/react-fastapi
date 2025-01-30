from sqlalchemy import Column, Float, Integer, String

from db.database import Base


class SalesTable(Base):
    __tablename__ = "sales"

    year = Column(Integer, primary_key=True, index=True)
    department = Column(String, primary_key=True, index=True)
    sales = Column(Float)
