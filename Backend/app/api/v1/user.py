from typing import Union

from fastapi import APIRouter, Query
from starlette import status

from app.database.transaction.utils import transactional
from app.schema.user import User
from app.services import UserService

user_router = APIRouter(prefix="/user", tags=["users"])
user_service = UserService()


@user_router.get(
    "/{user_id}", status_code=status.HTTP_200_OK, response_model=Union[User, None]
)
@transactional
async def get_user_by_id(user_id: int):
    return await user_service.get_user(user_id=user_id)
