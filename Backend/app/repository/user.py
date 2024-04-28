import uuid
from abc import ABC
from typing import Callable, List

from sqlalchemy import select, update, delete, exists
from sqlalchemy.ext.asyncio import AsyncSession

from app.schema.user import UserCreate, User, UserUpdate
from app.entity.user import UserEntity


class UserBaseRepository(ABC):

    async def get_user_by_email(self, email: str) -> User | None:
        pass

    async def get_user_by_id(self, user_id: uuid.UUID) -> User | None:
        pass

    async def create_user(self, user: User) -> None:
        pass

    async def update_user_by_id(self, user_id: uuid.UUID, user: User) -> User:
        pass

    async def delete_user_by_id(self, user_id: uuid.UUID) -> bool:
        pass

    async def get_all_user(self) -> List[User] | None:
        pass

    async def check_user_by_id(self, user_id: uuid.UUID) -> bool:
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

    async def get_user_by_email(self, email: str) -> User | None:
        query = await self.db.execute(
            select(UserEntity).where(UserEntity.email == email)
        )
        result = query.scalar_one_or_none()

        if result is None:
            return None
        return User.model_validate(result)

    async def get_all_user(self) -> List[User] | None:
        query = await self.db.execute(select(UserEntity))
        results = query.scalars().all()

        if not results:
            return None

        return [User.model_validate(result) for result in results]

    async def get_user_by_id(self, user_id: uuid.UUID) -> User | None:
        query = await self.db.execute(
            select(UserEntity).where(UserEntity.id == user_id)
        )
        result = query.scalar()

        if result is None:
            return None

        return User.model_validate(result)

    async def check_user_by_id(self, user_id: uuid.UUID) -> bool:
        return await self.db.scalar(select(exists().where(UserEntity.id == user_id)))

    async def create_user(self, user: UserCreate) -> None:
        self.db.add(UserEntity(**user.dict()))

    async def update_user_by_id(self, user_id: uuid.UUID, user: UserUpdate) -> bool:
        result = await self.db.execute(
            update(UserEntity)
            .where(UserEntity.id == user_id)
            .values(**user.dict(exclude_unset=True))
        )

        return result.rowcount > 0

    async def delete_user_by_id(self, user_id: uuid.UUID) -> bool:
        result = await self.db.execute(
            delete(UserEntity).where(UserEntity.id == user_id)
        )

        return result.rowcount > 0
