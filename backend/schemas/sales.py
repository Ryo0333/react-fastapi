from pydantic import BaseModel


class SalesBase(BaseModel):
    year: int
    department: str
    sales: float


class SalesCreate(SalesBase):
    pass


class SalesUpdate(SalesBase):
    class Config:
        orm_mode = True


class Sales(SalesBase):
    class Config:
        orm_mode = True
