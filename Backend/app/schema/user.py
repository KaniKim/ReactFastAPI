import datetime

from pydantic import BaseModel, EmailStr

from app.choice.user import ROLE


class UserLogin(BaseModel):
    email: EmailStr
    password: str
    first_name: str
    last_name: str
    nick_name: str | None


class User(UserLogin):
    id: int
    phone_number: str | None
    role: ROLE
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        from_attributes = True
