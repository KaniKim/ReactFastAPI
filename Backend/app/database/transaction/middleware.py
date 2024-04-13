from typing import Callable, Awaitable

from starlette import status
from starlette.requests import Request
from starlette.responses import Response

from app.database.transaction._session import sessionmanager


async def session_middleware(
    request: Request, call_next: Callable[[Request], Awaitable[Response]]
) -> Response:
    response = Response(
        "Internal server error", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
    )

    try:
        sessionmanager.set_db_session_context(session_id=hash(request))
        response = await call_next(request)
    finally:
        await sessionmanager.session.remove()
        sessionmanager.set_db_session_context(session_id=None)

    return response
