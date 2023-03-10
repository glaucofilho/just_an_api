from apis.version1.route_login import get_current_user_from_token
from db.models.users import User
from db.repository.users import create_new_user
from db.repository.users import update_password
from db.session import get_db
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from schemas.users import ShowUpdatePassword
from schemas.users import ShowUser
from schemas.users import UpdatePassword
from schemas.users import UserCreate
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/", response_model=ShowUser)
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user_from_token),
):
    if current_user.is_superuser:
        user = create_new_user(user=user, db=db)
        return user
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="You are not permitted!!!!"
        )


@router.post("/updatepassword", response_model=ShowUpdatePassword)
def update_pass(
    user: UpdatePassword,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user_from_token),
):
    if current_user.username == user.username or current_user.is_superuser == True:
        user = update_password(user=user, db=db)
        return user
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="You are not permitted!!!!"
        )
