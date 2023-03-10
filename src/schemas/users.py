from pydantic import BaseModel
from pydantic import EmailStr


# properties required during user creation
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    is_superuser: bool = False


class ShowUser(BaseModel):
    username: str
    email: EmailStr
    is_active: bool

    class Config:  # to convert non dict obj to json
        orm_mode = True


class UpdatePassword(BaseModel):
    username: str
    password: str


class UpdateSuperuser(BaseModel):
    username: str
    is_superuser: bool


class UpdateActive(BaseModel):
    username: str
    is_active: bool


class ShowUpdate(BaseModel):
    status: str
    username: str
