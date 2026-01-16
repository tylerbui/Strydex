import uuid
from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TokenPayload(BaseModel):
    sub: uuid.UUID | None = None


class Message(BaseModel):
    message: str


class NewPassword(BaseModel):
    token: str
    new_password: str
