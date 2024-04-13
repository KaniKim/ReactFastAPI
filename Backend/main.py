from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware

from app.api import api_router
from app.database.transaction.middleware import session_middleware

app = FastAPI()

app.include_router(api_router)
app.add_middleware(BaseHTTPMiddleware, dispatch=session_middleware)
