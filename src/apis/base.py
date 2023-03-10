from apis.version1 import route_actions
from apis.version1 import route_login
from apis.version1 import route_users
from fastapi import APIRouter


api_router = APIRouter()
api_router.include_router(route_login.router, prefix="/login", tags=["Authentication"])
api_router.include_router(
    route_users.router, prefix="/users", tags=["User Administration"]
)
api_router.include_router(route_actions.router, prefix="/data", tags=["Actions"])
