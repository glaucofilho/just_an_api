from core.hashing import Hasher
from db.models.users import User
from schemas.users import UpdatePassword
from schemas.users import UserCreate
from sqlalchemy.orm import Session


def create_new_user(user: UserCreate, db: Session):
    user = User(
        username=user.username,
        email=user.email,
        hashed_password=Hasher.get_password_hash(user.password),
        is_active=True,
        is_superuser=user.is_superuser,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def update_password(user: UpdatePassword, db: Session):
    db.query(User).filter(User.username == user.username).update(
        {User.hashed_password: Hasher.get_password_hash(user.password)}
    )
    db.commit()
    return {"status": "Sucess", "username": user.username}
