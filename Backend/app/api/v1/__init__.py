from fastapi import APIRouter

from app.api.v1.user import user_router

version_router = APIRouter(prefix="/v1", tags=["v1"])
version_router.include_router(user_router)
