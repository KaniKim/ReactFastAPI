import datetime

from sqlalchemy import Column, Integer, String, DateTime, UUID

from app.choice.user import ROLE
from app.entity import Base


class UserEntity(Base):
    __tablename__ = "user"

    id = Column(UUID, primary_key=True, server_default="gen_random_uuid()")
    nick_name = Column(String(length=255), nullable=True)
    email = Column(String(length=255), nullable=False)
    password = Column(String(length=255), nullable=False)
    first_name = Column(String(length=255), nullable=False)
    last_name = Column(String(length=255), nullable=False)
    phone_number = Column(String(length=255), nullable=True)
    role = Column(String(length=255), nullable=True, default=ROLE.NORMAL)
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.now)
    updated_at = Column(DateTime, nullable=False, default=datetime.datetime.now)
