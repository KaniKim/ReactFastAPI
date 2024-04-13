from fastapi import APIRouter

from app.api.v1 import version_router

api_router = APIRouter(prefix="/api", tags=["api"])
api_router.include_router(version_router)
