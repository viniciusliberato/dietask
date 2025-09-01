from datetime import datetime
import enum
from sqlalchemy import Column, Integer, String, DateTime, Enum, func, UniqueConstraint
from backend.db import Base  # importa a Base que criamos

class UserRole(str, enum.Enum):
    NUTRITIONIST = "NUTRITIONIST"
    PATIENT = "PATIENT"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    role = Column(Enum(UserRole), nullable=False, default=UserRole.PATIENT)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    accepted_terms_at = Column(DateTime(timezone=True), nullable=True)

    __table_args__ = (
        UniqueConstraint("email", name="uq_users_email"),
    )