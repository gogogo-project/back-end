from sqlalchemy import ForeignKey, Integer, Enum, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.domain.models.enums.trip_enum import TripStatusEnum
from app.domain.models.mixins.timestamp_mixin import TimestampMixin
from app.domain.models.mixins.trip_mixin import TripMixin
from app.infrastructure.database import Base


class Trip(Base, TripMixin, TimestampMixin):
    __tablename__ = "trips"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    driver_id: Mapped[int] = mapped_column(ForeignKey("drivers.id"), nullable=False)
    car_model: Mapped[str] = mapped_column(String(255), nullable=False)
    car_number: Mapped[str] = mapped_column(String(50), nullable=False, unique=False)
    number_of_seats: Mapped[int] = mapped_column(Integer, nullable=False)

    driver: Mapped["Driver"] = relationship("Driver", back_populates="trips")
    passengers: Mapped[list["TripPassenger"]] = relationship("TripPassenger", back_populates="trip")


class TripPassenger(Base, TripMixin):
    __tablename__ = "trip_passengers"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    trip_id: Mapped[int] = mapped_column(ForeignKey("trips.id"), nullable=False)
    passenger_id: Mapped[int] = mapped_column(ForeignKey("passengers.id"), nullable=False)
    status: Mapped[TripStatusEnum] = mapped_column(Enum(TripStatusEnum), default=TripStatusEnum.PENDING)

    trip: Mapped["Trip"] = relationship("Trip", back_populates="passengers")
    passenger: Mapped["Passenger"] = relationship("Passenger", back_populates="trips")
