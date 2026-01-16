from fastapi import APIRouter

from app.features.auth.api import routes as auth_routes
from app.features.users.api import routes as user_routes
from app.api.routes import items, private, utils
from app.core.config import settings

api_router = APIRouter()
api_router.include_router(auth_routes.router)
api_router.include_router(user_routes.router)
api_router.include_router(utils.router)
api_router.include_router(items.router)


if settings.ENVIRONMENT == "local":
    api_router.include_router(private.router)
