import datetime
import uuid
from typing import Optional

from pydantic import BaseModel, EmailStr, ConfigDict

from app.choice.user import ROLE


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    first_name: str
    last_name: str


class UserUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    phone_number: str | None = None
    nick_name: str | None = None
    role: str | None = None


class User(UserCreate):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    phone_number: str | None
    nick_name: str | None
    role: str
    created_at: datetime.datetime | None
    updated_at: datetime.datetime | None
