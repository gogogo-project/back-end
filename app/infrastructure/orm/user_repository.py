from typing import Optional, Callable, overload, Union

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.domain.models import User
from app.domain.repositories.user_repository import UserRepository
from app.infrastructure.orm.queries import (
    filter_user_by_telegram_id,
    filter_user_by_email,
    filter_user_by_id,
    get_user_by_telegram_id,
    get_user_by_email,
    get_user_by_phone_number,
)


class SQLUserRepository(UserRepository):

    filter_map: dict[str, Callable] = {
        'id': filter_user_by_id,
        'telegram_id': filter_user_by_telegram_id,
        'email': filter_user_by_email,
    }

    auth_field_map = {
        "telegram": get_user_by_telegram_id,
        "email": get_user_by_email,
        "phone": get_user_by_phone_number
    }

    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_user(self, user_data: dict) -> User:
        user = User(**user_data)
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user

    async def get_user_by_telegram_id(self, telegram_id: str) -> User | None:
        async with self.db as session:
            user: Optional[User] = await get_user_by_telegram_id(session=session, telegram_id=telegram_id)
            return user

    async def get_user_by_user_id(self, user_id: str) -> User | None:
        stmt = select(User).where(User.id == user_id)
        result = await self.db.execute(stmt)
        return result.scalar_one_or_none()

    @overload
    async def is_user_exists(self, *, id: Union[str, int]) -> bool: ...

    @overload
    async def is_user_exists(self, *, telegram_id: Union[str, int]) -> bool: ...

    @overload
    async def is_user_exists(self, *, email: str) -> bool: ...

    async def is_user_exists(self, **kwargs) -> bool:
        try:
            identifier_type, identifier_value = next(filter(lambda item: item[1], kwargs.items()))
        except StopIteration:
            raise ValueError('id or telegram_id or email are required')

        if identifier_type not in self.filter_map:
            raise ValueError('only params id or telegram_id or email are required')

        async with self.db as session:
            user: Optional[User] = (await self.filter_map[identifier_type](session, identifier_value)).one_or_none()

        return True if user else False

    async def get_user_by_auth_method(self, auth_method: str, identifier: str | int) -> User | None:
        if auth_method not in self.auth_field_map:
            raise ValueError(f"Unsupported authentication method: {auth_method}")

        async with self.db as session:
            user = await self.auth_field_map[auth_method](session, identifier)

        return user.scalars().first()
