from sqlalchemy.orm import Session

from core.security import get_password_hash
from models.user import UserTable
from schemas.user import UserCreate, UserInDB


def create_admin(db: Session, user: UserCreate) -> UserInDB:
    hashed_password = get_password_hash(user.password)
    db_user = UserInDB(name=user.name, password=hashed_password, role="admin")
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_admin_by_name(db: Session, name: str) -> UserInDB:
    return db.query(UserTable).filter(UserInDB.name == name).first()


def get_admin(db: Session, name: str) -> UserInDB:
    return db.query(UserTable).filter(UserInDB.name == name).first()
