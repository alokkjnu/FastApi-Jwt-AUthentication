from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Text, func, UniqueConstraint
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base
import json
from sqlalchemy.dialects.postgresql import UUID
import uuid


class BaseClass(Base):

    __abstract__ = True

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    name = Column(String(50), unique=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

class Role(BaseClass):
    __tablename__ = "roles"

    __table_args__ = {'extend_existing': True}

    name = Column(String(50), unique=True)