"""
Central model registry.
This module imports all models to ensure they are registered with SQLModel.
Required for Alembic migrations and app startup.
"""
from app.shared.database.base import Base

# Import all models here to register them with SQLModel
from app.features.users.models import User

__all__ = ["Base", "User"]
