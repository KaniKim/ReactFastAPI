import uuid
from typing import Union, List, Annotated

from fastapi import APIRouter, Depends
from starlette import status
from starlette.responses import JSONResponse, Response

from app.database.transaction.utils import transactional
from app.middleware.security import get_current_user
from app.schema.security import Token
from app.schema.user import User, UserCreate, UserUpdate
from app.services.token import TokenService
from app.services.user import UserService

user_router = APIRouter(prefix="/user", tags=["users"])
user_service = UserService()
token_service = TokenService()


@user_router.post("/token", status_code=status.HTTP_201_CREATED, response_model=Token)
@transactional
async def login_for_access_token(email: str, password: str) -> Token | JSONResponse:
    if token_service.authenticate_user(email=email, password=password):
        data = {"email": email}
        access_token = token_service.create_access_token(data=data)
        refresh_token = token_service.create_refresh_token(data=data)
        return Token(
            access_token=access_token, refresh_token=refresh_token, token_type="Bearer"
        )

    return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED,
        content={"message": "User information is not correct"},
    )


@user_router.get(
    "/{user_id}", status_code=status.HTTP_200_OK, response_model=Union[User, None]
)
@transactional
async def get_user_by_id(user_id: uuid.UUID):
    return await user_service.get_user(user_id=user_id)


@user_router.get(
    "/", status_code=status.HTTP_200_OK, response_model=Union[List[User], None]
)
@transactional
async def get_all_users():
    return await user_service.get_user(user_id=None)


@user_router.post("/", status_code=status.HTTP_201_CREATED, response_model=None)
@transactional
async def create_user(user: UserCreate):
    return await user_service.create_user(user)


@user_router.put("/{user_id}", status_code=status.HTTP_200_OK, response_model=User)
@transactional
async def update_user(user_id: uuid.UUID, user: UserUpdate):
    result = await user_service.update_user(user_id=user_id, user=user)
    return (
        result
        if result
        else JSONResponse(
            content={"message": "User is not updated"},
            status_code=status.HTTP_400_BAD_REQUEST,
        )
    )


@user_router.delete(
    "/{user_id}", status_code=status.HTTP_204_NO_CONTENT, response_class=Response
)
@transactional
async def delete_user(user_id: uuid.UUID):
    if await user_service.delete_user(user_id=user_id):
        return JSONResponse(
            content={"message": "User is deleted"},
            status_code=status.HTTP_204_NO_CONTENT,
        )
    return JSONResponse(
        content={"message": "User is not deleted"},
        status_code=status.HTTP_404_NOT_FOUND,
    )


@user_router.get("/me", status_code=status.HTTP_200_OK, response_model=User)
@transactional
async def get_user_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user
