from datetime import datetime
from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Float, String, DateTime


class TripMixin:
    origin: Mapped[str] = mapped_column(String(255), nullable=False)
    start_lat: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    start_lon: Mapped[Optional[float]] = mapped_column(Float, nullable=True)

    destination: Mapped[str] = mapped_column(String(255), nullable=False)
    end_lat: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    end_lon: Mapped[Optional[float]] = mapped_column(Float, nullable=True)

    start_time: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    end_time: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
