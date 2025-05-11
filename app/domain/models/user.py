from typing import Optional
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, ForeignKey, Float, Integer, BigInteger
from app.infrastructure.database import Base
from app.domain.models.mixins.timestamp_mixin import TimestampMixin


class User(Base, TimestampMixin):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    telegram_id: Mapped[Optional[int]] = mapped_column(BigInteger, unique=True, nullable=True)  # For Telegram users
    name: Mapped[str] = mapped_column(String(64))
    username: Mapped[Optional[str]] = mapped_column(String(64), unique=True, nullable=True)  # Telegram or app username
    email: Mapped[Optional[str]] = mapped_column(String(64), unique=True, nullable=True)  # Mobile app users
    phone_number: Mapped[Optional[str]] = mapped_column(String(64), unique=True, nullable=True)  # OTP login
    password: Mapped[Optional[str]] = mapped_column(String(64), nullable=True)  # Only needed for email/password users
    auth_method: Mapped[str] = mapped_column(String(16), nullable=False)  # ['telegram', 'phone', 'email', 'oauth']
    is_blocked: Mapped[bool] = mapped_column(default=False)
    language_code: Mapped[str | None] = mapped_column(String(4))

    driver_profile: Mapped["Driver"] = relationship("Driver", back_populates="user", uselist=False)
    passenger_profile: Mapped["Passenger"] = relationship("Passenger", back_populates="user", uselist=False)


class Passenger(Base):
    __tablename__ = "passengers"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False, unique=True)
    number_of_seats: Mapped[int] = mapped_column(Integer, default=1)
    person_to_notify: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)

    user: Mapped["User"] = relationship("User", back_populates="passenger_profile")
    trips: Mapped[list["TripPassenger"]] = relationship("TripPassenger", back_populates="passenger")


class Driver(Base):
    __tablename__ = "drivers"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False, unique=True)
    rating: Mapped[Optional[float]] = mapped_column(Float, default=5.0)

    user: Mapped["User"] = relationship("User", back_populates="driver_profile")
    trips: Mapped[list["Trip"]] = relationship("Trip", back_populates="driver")
