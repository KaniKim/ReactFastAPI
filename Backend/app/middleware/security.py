import os
from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from starlette import status
from starlette.exceptions import HTTPException

from app.choice.user import ROLE
from app.repository.user import UserRepository
from app.schema.user import User

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")


async def get_current_user(
    token: Annotated[str, Depends(OAuth2PasswordBearer(tokenUrl="token"))]
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("email")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = user_repo.get_user_by_email(email=email)
    if user is None:
        raise credentials_exception
    return user


async def get_current_not_normal(
    current_user: Annotated[User, Depends(get_current_user)],
) -> bool:
    if current_user.role == ROLE.SUPERUSER:
        return ROLE.SUPERUSER
    if current_user.role == ROLE.STAFF:
        return ROLE.STAFF
    return ROLE.NORMAL
