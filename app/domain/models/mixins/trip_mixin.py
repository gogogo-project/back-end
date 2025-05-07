from datetime import datetime
from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Float, String, DateTime


class TripMixin:
    origin: Mapped[str] = mapped_column(String(255), nullable=False)
    origin_stipped: Mapped[str] = mapped_column(String(255), nullable=False)

    start_lat: Mapped[float] = mapped_column(Float, nullable=True)
    start_lon: Mapped[float] = mapped_column(Float, nullable=True)

    destination: Mapped[str] = mapped_column(String(255), nullable=False)
    destination_stipped: Mapped[str] = mapped_column(String(255), nullable=False)

    end_lat: Mapped[float] = mapped_column(Float, nullable=True)
    end_lon: Mapped[float] = mapped_column(Float, nullable=True)

    start_time: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)
    end_time: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)
