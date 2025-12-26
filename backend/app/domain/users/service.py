from fastapi import HTTPException

from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from app.core.security import get_password_hash
from app.domain.users.schemas import UserCreate
from app.models import User


async def create_user(
    *,
    db: AsyncSession,
    payload: UserCreate,
) -> User:
    # Check if user with this email already exists
    statement = select(User).where(User.email == payload.email)
    result = await db.exec(statement)
    existing_user = result.first()
    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists in the system",
        )
    
    # Create new user with hashed password
    db_user = User.model_validate(
        payload, update={"hashed_password": get_password_hash(payload.password.get_secret_value())}
    )
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user