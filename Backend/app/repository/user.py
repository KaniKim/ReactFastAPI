from abc import ABC
from typing import Callable

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.schema.user import User
from app.entity.user import UserEntity


class UserBaseRepository(ABC):
    async def get_user_by_id(self, user_id: int) -> User | None:
        pass

    async def create_user(self, user: User) -> User:
        pass

    async def update_user_by_id(self, user_id: int, user: User) -> User:
        pass

    async def delete_user_by_id(self, user_id: int) -> None:
        pass


class UserRepository(UserBaseRepository):

    def __init__(
        self,
        session_or_factory: AsyncSession | Callable[[], AsyncSession],
    ) -> None:
        self._session_or_factory = session_or_factory

    @property
    def db(self) -> AsyncSession:
        if isinstance(self._session_or_factory, AsyncSession):
            return self._session_or_factory
        return self._session_or_factory()

    async def get_user_by_id(self, user_id: int) -> User | None:
        query = await self.db.execute(
            select(UserEntity).where(UserEntity.id == user_id)
        )
        result = query.one_or_none()

        if result is None:
            return None

        return User.from_orm(result)
