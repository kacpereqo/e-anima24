from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class UserRegister(BaseModel):
    username: str
    email: str
    provider: str
    verifier: str


class User(BaseModel):
    username: str
    email: str
    verifier: str
    provider: str
    avatar: str
