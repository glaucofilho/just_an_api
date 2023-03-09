from core.config import settings
from core.hashing import Hasher
from sqlalchemy import create_engine


def create_super_user(user, passw, email):
    if settings.USE_SQLITE_DB == "True":
        SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
        engine = create_engine(
            SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
        )
    else:
        SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
        engine = create_engine(SQLALCHEMY_DATABASE_URL)

    super = engine.execute("SELECT username FROM user WHERE username = 'sa'")

    super = [row[0] for row in super]

    if not super:
        engine.execute(
            "INSERT INTO user (username, email, hashed_password, is_active, is_superuser) VALUES (:username, :email, :hashed_password, :is_active, :is_superuser)",
            username=user,
            email=email,
            hashed_password=Hasher.get_password_hash(passw),
            is_active=True,
            is_superuser=True,
        )
