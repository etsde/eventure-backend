from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, CheckConstraint
from sqlalchemy.sql import func
from .database import Base

class Inventory(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    quantity = Column(Integer, default=1)
    status = Column(String, default="Verfügbar")
    description = Column(Text, nullable=True)
    created_at = Column(TIMESTAMP, server_default=func.now())

    __table_args__ = (
        CheckConstraint("type IN ('Technik', 'Bar')"),
        CheckConstraint("status IN ('Verfügbar', 'Ausgeliehen')"),
    )
