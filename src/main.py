from apis.base import api_router
from core.config import settings
from db.base import Base
from db.session import engine
from db.super_user import create_super_user
from db.utils import check_db_connected
from db.utils import check_db_disconnected
from fastapi import FastAPI


def include_router(app):
    app.include_router(api_router)


def create_tables():
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.PROJECT_VERSION,
        swagger_ui_parameters={"defaultModelsExpandDepth": -1},
    )
    include_router(app)
    create_tables()
    create_super_user(settings.ADMIN_USER, settings.ADMIN_PASS, settings.ADMIN_EMAIL)
    return app


app = start_application()


@app.on_event("startup")
async def app_startup():
    await check_db_connected()


@app.on_event("shutdown")
async def app_shutdown():
    await check_db_disconnected()
