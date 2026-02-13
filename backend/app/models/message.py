import uuid
from sqlalchemy import String, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
from app.core.db import Base

class Message(Base):
    __tablename__ = "messages"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), 
        primary_key=True, 
        default=uuid.uuid4
    )
    business_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), 
        ForeignKey("businesses.id"), 
        nullable=False
    )
    customer_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), 
        ForeignKey("customers.id"), 
        nullable=False
    )
    direction: Mapped[str] = mapped_column(
        String(10), 
        nullable=False
    )  # "IN" or "OUT"
    text: Mapped[str | None] = mapped_column(Text, nullable=True)