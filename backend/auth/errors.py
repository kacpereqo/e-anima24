from fastapi import HTTPException, status

incorect_credentials_error = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Incorrect username or password",
    headers={"WWW-Authenticate": "Bearer"},
)

user_already_exists_error = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="User with this username already exists",
)
