import uuid
from typing import List

from passlib.context import CryptContext

from app.database.transaction.session import sessionmanager
from app.repository.user import UserRepository
from app.schema.user import User, UserCreate, UserUpdate


class UserService:
    user_repo = UserRepository(session_or_factory=sessionmanager.get_current_session)
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    async def get_user(self, user_id: uuid.UUID | None) -> User | List[User] | None:
        if user_id:
            result = await self.user_repo.get_user_by_id(user_id=user_id)
        else:
            result = await self.user_repo.get_all_user()

        return result

    async def update_user(self, user_id: uuid.UUID, user: UserUpdate) -> User | None:
        if await self.user_repo.check_user_by_id(user_id=user_id):
            await self.user_repo.update_user_by_id(user_id=user_id, user=user)
            return await self.user_repo.get_user_by_id(user_id=user_id)
        return None

    async def delete_user(self, user_id: uuid.UUID) -> bool:
        if await self.user_repo.check_user_by_id(user_id=user_id):
            return await self.user_repo.delete_user_by_id(user_id=user_id)
        return False

    async def create_user(self, user: UserCreate) -> None:
        user.password = self.pwd_context.hash(user.password)
        await self.user_repo.create_user(user)