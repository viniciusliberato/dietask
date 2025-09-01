from sqlalchemy import Column, Integer, ForeignKey, DateTime, func
from backend.db import Base

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, autoincrement=True)

    # user_id = o usuário que é o paciente
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    # nutritionist_id = o usuário que é o nutricionista desse paciente
    nutritionist_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
