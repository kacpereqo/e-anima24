from datetime import datetime, timedelta
from typing import Annotated

import google_auth_oauthlib.flow
from db.database import db
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from googleapiclient.discovery import build
from jose import JWTError, jwt
from passlib.context import CryptContext
from starlette.responses import RedirectResponse

from .errors import user_already_exists_error
from .models import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")


class AuthService:
    def __init__(self):
        self.secret_key = (
            "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
        )
        self.algorithm = "HS256"
        self.token_expire_time = 30

    def verify_password(self, plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password):
        return pwd_context.hash(password)

    def authenticate_user(self, username: str, password: str):
        user = db.get_user_by_email_or_username(username)
        if user is None:
            return False
        if not self.verify_password(password, user.hashed_password):
            return False
        return user

    def create_access_token(self, data: dict):
        to_encode = data.copy()
        expires_delta = timedelta(minutes=self.token_expire_time)

        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, self.secret_key, algorithm=self.algorithm)
        return encoded_jwt

    async def get_current_user(self, token: Annotated[str, Depends(oauth2_scheme)]):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            username: str = payload.get("sub")
            if username is None:
                raise credentials_exception
        except JWTError:
            raise credentials_exception
        user = db.get_user(username)
        if user is None:
            raise credentials_exception
        return user

    def register_new_user(self, new_user):
        is_unique = db.check_unique_credentials(new_user.username, new_user.email)
        if not is_unique:
            raise user_already_exists_error

        hashed_password = self.get_password_hash(new_user.password)
        db.add_new_user(new_user, hashed_password)

    def google_auth(self, request):
        state = request.session.get("state", None)

        flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
            "client_secret.json",
            scopes=[
                "https://www.googleapis.com/auth/userinfo.email",
                "https://www.googleapis.com/auth/userinfo.profile",
                "openid",
            ],
            state=state,
        )
        flow.redirect_uri = "http://localhost:3000/auth/callback/google"
        authorization_response = str(request.url)

        flow.fetch_token(authorization_response=authorization_response)

        credentials = flow.credentials
        request.session["credentials"] = {
            "token": credentials.token,
            "refresh_token": credentials.refresh_token,
            "token_uri": credentials.token_uri,
            "client_id": credentials.client_id,
            "client_secret": credentials.client_secret,
            "scopes": credentials.scopes,
        }

        oauth_service = build("oauth2", "v2", credentials=credentials)
        ouath2_user_info = oauth_service.userinfo().get().execute()

        user = db.get_user_by_email(ouath2_user_info["email"])
        if user is None:
            new_user = User(
                username=ouath2_user_info.get("given_name", credentials._id_token),
                email=ouath2_user_info["email"],
                verifier=credentials._id_token,
                provider="google",
                avatar=ouath2_user_info["picture"],
            )
            user = db.add_new_user(new_user)

        jwt = self.create_access_token(data={"sub": user.email})

        return {
            "access_token": jwt,
            "user": {
                "username": user.username,
                "email": user.email,
                "userId": user.user_id,
                "avatar": user.avatar,
            },
        }
