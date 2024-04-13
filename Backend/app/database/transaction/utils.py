import functools
from typing import Awaitable, Callable

from app.database.transaction._session import sessionmanager

AsyncCallable = Callable[..., Awaitable]


def transactional(func: AsyncCallable) -> AsyncCallable:
    @functools.wraps(func)
    async def _wrapper(*args, **kwargs):
        try:
            session = sessionmanager.session()

            if session.in_transaction():
                return await func(*args, **kwargs)

            async with session.begin():
                return_value = await func(*args, **kwargs)

            return return_value
        except Exception as e:
            raise e

    return _wrapper
