from fastapi import APIRouter, Depends, Response, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from .errors import incorect_credentials_error
from .models import User
from .service import AuthService

router = APIRouter()
auth = AuthService()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


@router.post("/login")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = auth.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise incorect_credentials_error
    jwt = auth.create_access_token(data={"sub": user.username})

    return {"access_token": jwt, "token_type": "bearer"}


@router.get("/users/me/")
async def read_users_me(current_user: User = Depends(auth.get_current_user)):
    return current_user


@router.post("/register")
async def register_user(user: User):
    auth.register_new_user(user)
    return status.HTTP_201_CREATED
