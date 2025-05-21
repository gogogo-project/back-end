from typing import Union

from sqlalchemy import desc
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload

from app.domain.models import User, Driver, Trip, Passenger


async def filter_user_by_id(session: AsyncSession, user_id: int | str):
    return await session.scalars(select(User).filter_by(id=user_id))


async def filter_user_by_telegram_id(session: AsyncSession, telegram_id: int | str):
    return await session.execute(select(User).filter_by(telegram_id=telegram_id))


async def filter_user_by_email(session: AsyncSession, email: str):
    return await session.execute(select(User).filter_by(email=email))


async def get_user_by_phone_number(session: AsyncSession, phone_number: str):
    return await session.execute(select(User).where(User.phone_number == phone_number))


async def get_user_by_telegram_id(session: AsyncSession, telegram_id: int):
    result = await session.execute(
        select(User)
        .where(User.telegram_id == telegram_id)
    )
    return result.scalar_one_or_none()


async def get_user_by_email(session: AsyncSession, email: str):
    return await session.execute(select(User).where(User.email == email))


async def get_driver_by_id(session: AsyncSession, driver_id: int) -> Union[Driver, None]:
    result = await session.execute(select(Driver).where(id=driver_id))
    return result.scalar_one_or_none()


async def get_driver_by_user_id(session: AsyncSession, user_id: int) -> Union[Driver, None]:
    result = await session.execute(
        select(Driver)
        .options(selectinload(Driver.user))
        .where(Driver.user_id == user_id)
    )
    return result.scalar_one_or_none()


async def get_trips(session: AsyncSession, driver_id: int) -> Union[list[Trip], None]:
    result = await session.execute(
        select(Trip).where(
            Trip.driver_id == driver_id
        ).order_by(
            desc(Trip.created_at)
        ).limit(5)
    )
    return result.scalars().all()


async def get_passenger_by_user_id(session: AsyncSession, user_id: int) -> Union[Passenger, None]:
    result = await session.execute(
        select(Passenger)
        .options(selectinload(Passenger.user))
        .where(Passenger.user_id == user_id)
    )
    return result.scalar_one_or_none()
