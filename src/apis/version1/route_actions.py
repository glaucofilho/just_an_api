from datetime import datetime

from apis.version1.route_login import get_current_user_from_token
from db.models.users import User
from db.session import get_db
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/time")
def get_datetime(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user_from_token),
):
    if current_user.is_active:
        return datetime.now()

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="You are disable!",
    )
