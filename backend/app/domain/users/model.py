from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from datetime import datetime
from sqlmodel import DateTime

class User(DeclarativeBase):
    __tablename__ = "users"

    id: Mapped[int] =mapped_column(primary_key= True, unique= True, index= True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index= True)
    name: Mapped[str] = mapped_column(min_length=1, max_length=255)
    password: Mapped[str] = mapped_column(String(255), min_length=8, max_length=15, unique=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)



    
