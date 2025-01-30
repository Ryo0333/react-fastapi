from passlib.context import CryptContext
from sqlalchemy.orm import Session

from schemas.user import User, UserCreate, UserInDB

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    return pwd_context.hash(password)


def get_users(db: Session):
    return db.query(User).all()


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_name(db: Session, name: str) -> UserInDB:
    return db.query(User).filter(User.name == name).first()


def get_user_by_name_by_password(db: Session, name: str, password: str):
    return (
        db.query(User)
        .filter(User.name == name)
        .filter(User.password == password)
        .first()
    )


def create_user(db: Session, user: UserCreate) -> UserInDB:
    hashed_password = get_password_hash(user.password)
    db_user = User(name=user.name, password=hashed_password, role="user")
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_admin(db: Session, user: UserCreate) -> UserInDB:
    hashed_password = get_password_hash(user.password)
    db_user = User(name=user.name, password=hashed_password, role="admin")
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
