import uuid
from typing import List

from passlib.context import CryptContext

from app.choice.user import ROLE
from app.database.transaction._session import sessionmanager
from app.repository.user import UserRepository
from app.schema.user import User, UserCreate


class UserService:
    user_repo = UserRepository(session_or_factory=sessionmanager.get_current_session)
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    async def get_user(self, user_id: uuid.UUID | None) -> User | List[User] | None:
        if user_id:
            result = await self.user_repo.get_user_by_id(user_id=user_id)
        else:
            result = await self.user_repo.get_all_user()

        return result

    async def create_user(self, user: UserCreate) -> None:
        user.password = self.get_password_hash(user.password)
        await self.user_repo.create_user(user)

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return self.pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password: str) -> str:
        return self.pwd_context.hash(password)
