from typing import Union

from fastapi import APIRouter, Query
from starlette import status

from app.database.transaction.utils import transactional
from app.schema.user import User, UserLogin
from app.services.user import UserService

user_router = APIRouter(prefix="/user", tags=["users"])
user_service = UserService()


@user_router.get(
    "/{user_id}", status_code=status.HTTP_200_OK, response_model=Union[User, None]
)
async def get_user_by_id(user_id: int):
    return await user_service.get_user(user_id=user_id)


@user_router.post("/", status_code=status.HTTP_201_CREATED, response_model=None)
@transactional
async def create_user(user: UserLogin):
    pass
