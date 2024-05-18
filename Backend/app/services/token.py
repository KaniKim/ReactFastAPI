import datetime  # type: ignore
import os

from jose import jwt  # type: ignore
from passlib.context import CryptContext  # type: ignore

from app.database.transaction.session import sessionmanager
from app.repository.user import UserRepository


class TokenService:
    user_repo = UserRepository(session_or_factory=sessionmanager.get_current_session)
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    SECRET_KEY = os.getenv("SECRET_KEY")
    ALGORITHM = os.getenv("ALGORITHM")

    def _create_token(self, data: dict, expires_delta: int | None) -> str:
        to_encode = data.copy()

        if expires_delta:
            expire = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(
                minutes=expires_delta
            )
        else:
            expire = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(
                days=14
            )

        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)
        return encoded_jwt

    async def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)

    async def authenticate_user(self, email: str, password: str) -> bool:
        user = await self.user_repo.get_user_by_email(email=email)

        if not user:
            return False

        if not self.verify_password(password, user.password):
            return False

        return True

    async def create_refresh_token(self, data: dict) -> str:
        return self._create_token(data=data, expires_delta=None)

    async def create_access_token(
        self, data: dict, expires_delta: int | None = None
    ) -> str:
        return self._create_token(data=data, expires_delta=expires_delta)
