from sqlalchemy.orm import Session

from core.security import get_password_hash
from models.user import UserTable
from schemas.user import UserCreate, UserInDB


def get_users(db: Session):
    return db.query(UserTable).all()


def get_user(db: Session, user_id: int):
    return db.query(UserTable).filter(UserInDB.id == user_id).first()


def get_user_by_name(db: Session, name: str) -> UserInDB:
    return db.query(UserTable).filter(UserInDB.name == name).first()


def get_user_by_name_by_password(db: Session, name: str, password: str):
    return (
        db.query(UserTable)
        .filter(UserInDB.name == name)
        .filter(UserInDB.hashed_password == password)
        .first()
    )


def create_user(db: Session, user: UserCreate) -> UserInDB:
    hashed_password = get_password_hash(user.password)
    db_user = UserInDB(name=user.name, password=hashed_password, role="user")
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
