from sqlmodel import Session, select

from app.core.config import settings
from app.core.security import get_password_hash
from app.shared.database.session import engine, get_async_session
from app.shared.database.registry import User
from app.features.users.schemas.requests import UserCreate

# Make sure all models are imported via registry
# This ensures SQLModel knows about all models for migrations and relationships


def init_db(session: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next lines
    # from sqlmodel import SQLModel

    # This works because the models are already imported and registered from registry
    # SQLModel.metadata.create_all(engine)

    user = session.exec(
        select(User).where(User.email == settings.FIRST_SUPERUSER)
    ).first()
    if not user:
        user_in = UserCreate(
            email=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True,
        )
        # Inline user creation for sync initialization
        db_user = User.model_validate(
            user_in, update={"hashed_password": get_password_hash(user_in.password)}
        )
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
