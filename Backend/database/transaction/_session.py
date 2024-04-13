from contextvars import ContextVar
from typing import Optional

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_scoped_session,
    async_sessionmaker,
    create_async_engine,
    AsyncEngine,
)

from database.transaction import password, database, host, port, username


class DatabaseSessionManager:
    def __init__(self):
        self.engine: AsyncEngine | None = None
        self.session_maker = None
        self.session: AsyncSession | None = None
        self.db_session_context: ContextVar[Optional[int]] = ContextVar(
            "db_session_context", default=None
        )

    def init_db(
        self,
        username: str,
        password: str,
        host: str,
        port: int,
        database: str,
    ):
        self.engine = create_async_engine(
            f"postgresql+asyncpg://{username}:{password}@{host}:{port}/{database}"
        )

        self.session_maker = async_sessionmaker(
            autoflush=False, autocommit=False, bind=self.engine
        )

        self.session = async_scoped_session(
            self.session_maker, scopefunc=self.get_db_session_context
        )

    def get_db_session_context(self) -> int:
        session_id = self.db_session_context.get()

        if not session_id:
            raise ValueError("Currently no session is available")

        return session_id

    def set_db_session_context(self, *, session_id: int | None) -> None:
        self.db_session_context.set(session_id)

    def get_current_session(self) -> AsyncSession:
        return self.session

    async def close(self):
        if self.engine is None:
            raise Exception("DatabaseSessionManager is not initialized.")
        await self.engine.dispose()


sessionmanager = DatabaseSessionManager()
sessionmanager.init_db(
    username=username,
    password=password,
    host=host,
    port=port,
    database=database,
)
