from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.domain.models import User
from app.domain.repositories.user_repository import UserRepository


class SQLUserRepository(UserRepository):

    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_user(self, user_data: dict) -> User:
        user = User(**user_data)
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user

    async def get_user_by_telegram_id(self, telegram_id: str) -> User | None:
        stmt = select(User).where(User.telegram_id == telegram_id)
        result = await self.db.execute(stmt)
        return result.scalar_one_or_none()

    async def get_user_by_user_id(self, user_id: str) -> User | None:
        stmt = select(User).where(User.id == user_id)
        result = await self.db.execute(stmt)
        return result.scalar_one_or_none()

    async def is_user_exists(self, id: Optional[str] = None, telegram_id: Optional[str] = None) -> bool:
        if not (id or telegram_id):
            raise ValueError("id or telegram_id is required")

        async with self.db as session:
            user: Optional[User]
            if id:
                user = (await session.scalars(select(User).filter_by(id=id))).one_or_none()
                if user:
                    return True

            if telegram_id:
                user = (await session.scalars(select(User).filter_by(telegram_id=telegram_id))).one_or_none()
                if user:
                    return True

        return False
