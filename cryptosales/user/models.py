import uuid

from sqlalchemy import Column, Boolean, Integer, String
from sqlalchemy.dialects import postgresql

from core.database import BaseModel
from core.i18n import DEFAULT_LANGUAGE


class User(BaseModel):
    __tablename__ = "cryptosales_user"

    id: uuid.UUID = Column(postgresql.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    telegram_id: str = Column(Integer, unique=True, nullable=False)
    language: str = Column(String, default=DEFAULT_LANGUAGE)
    is_active: bool = Column(Boolean, default=True, nullable=False)
