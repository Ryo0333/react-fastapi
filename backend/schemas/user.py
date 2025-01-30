from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    role: str


class UserCreate(UserBase):
    password: str


class UserInDB(UserBase):
    id: int
    is_active: bool
    hashed_password: str

    class Config:
        orm_mode = True
