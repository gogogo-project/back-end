from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.domain.models import User


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
        select(User).where(User.telegram_id == telegram_id)
    )
    return result.scalar_one_or_none()


async def get_user_by_email(session: AsyncSession, email: str):
    return await session.execute(select(User).where(User.email == email))
