from apis.version1.route_login import get_current_user_from_token
from db.models.users import User
from db.repository.users import create_new_user
from db.repository.users import delete_username
from db.repository.users import update_active
from db.repository.users import update_password
from db.repository.users import update_superuser
from db.session import get_db
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from schemas.users import DeleteUser
from schemas.users import ShowUpdate
from schemas.users import ShowUser
from schemas.users import UpdateActive
from schemas.users import UpdatePassword
from schemas.users import UpdateSuperuser
from schemas.users import UserCreate
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/create", response_model=ShowUser)
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user_from_token),
):
    if current_user.is_active:
        if current_user.is_superuser:
            user = create_new_user(user=user, db=db)
            return user
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="You are not permitted!!!!",
            )
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="You are disable!",
    )


@router.post("/update/password", response_model=ShowUpdate)
def update_pass(
    user: UpdatePassword,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user_from_token),
):
    if current_user.is_active:
        if current_user.username == user.username or current_user.is_superuser == True:
            user = update_password(user=user, db=db)
            return user
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="You are not permitted!!!!",
            )
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="You are disable!",
    )


@router.post("/update/active", response_model=ShowUpdate)
def update_act(
    user: UpdateActive,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user_from_token),
):
    if current_user.is_active:
        if current_user.is_superuser == True:
            user = update_active(user=user, db=db)
            return user
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="You are not permitted!!!!",
            )
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="You are disable!",
    )


@router.post("/update/superuser", response_model=ShowUpdate)
def update_super(
    user: UpdateSuperuser,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user_from_token),
):
    if current_user.is_active:
        if current_user.is_superuser == True:
            user = update_superuser(user=user, db=db)
            return user
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="You are not permitted!!!!",
            )
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="You are disable!",
    )


@router.delete("/delete", response_model=ShowUpdate)
def delete_user(
    user: DeleteUser,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user_from_token),
):
    if current_user.is_active:
        if current_user.is_superuser == True:
            user = delete_username(user=user, db=db)
            return user
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="You are not permitted!!!!",
            )
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="You are disable!",
    )
