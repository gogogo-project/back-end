from sqlalchemy import TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime, timezone

def utc_now():
    return datetime.now(timezone.utc)

class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True), default=utc_now, nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True), default=utc_now, onupdate=utc_now, nullable=False
    )
