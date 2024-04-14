from passlib.context import CryptContext

from app.database.transaction._session import sessionmanager
from app.repository.user import UserRepository
from app.schema.user import User


class UserService:
    user_repo = UserRepository(session_or_factory=sessionmanager.get_current_session)
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    async def get_user(self, user_id: int) -> User | None:
        result = await self.user_repo.get_user_by_id(user_id=user_id)

        return result

    async def create_user(
        self,
        email: str,
        password: str,
        first_name: str,
        last_name: str,
        nick_name: str | None,
    ) -> None:
        self.user_repo.create_user()

    async def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return self.pwd_context.verify(plain_password, hashed_password)
