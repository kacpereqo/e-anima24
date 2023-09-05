from fastapi import HTTPException, status

incorect_credentials_error = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Incorrect username or password",
    headers={"WWW-Authenticate": "Bearer"},
)

user_already_exists_error = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Użytkownik z takim adresem email lub nazwą użytkownika już istnieje",
)

user_with_email_already_exists_error = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail={
        "data": {
            "elementName": "email",
            "error": "Użytkownik z takim emailem już istnieje",
        }
    },
)

user_with_username_already_exists_error = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail={
        "data": {
            "elementName": "username",
            "error": "Użytkownik z taką nazwą już istnieje",
        }
    },
)

#   data: {
# elementName: string;
# error: string;
# }
