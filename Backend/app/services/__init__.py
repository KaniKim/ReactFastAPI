from sqlalchemy.ext.asyncio import AsyncSession

from app.database.transaction._session import sessionmanager
from app.repository.user import UserRepository
from app.schema.user import User


class UserService:
    user_repo = UserRepository(session_or_factory=sessionmanager.get_current_session)

    async def get_user(self, user_id: int) -> User | None:
        result = await self.user_repo.get_user_by_id(user_id=user_id)

        return result
