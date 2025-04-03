from abc import ABC, abstractmethod
from typing import Optional

from app.domain.models import User


class UserRepository(ABC):
    @abstractmethod
    async def create_user(self, user_data: dict) -> User:
        pass

    @abstractmethod
    async def get_user_by_telegram_id(self, telegram_id: str) -> User | None:
        pass

    @abstractmethod
    async def get_user_by_user_id(self, user_id: str) -> User | None:
        pass

    @abstractmethod
    async def is_user_exists(
            self,
            id: Optional[str] = None,
            telegram_id: Optional[str] = None,
    ) -> bool:
        pass
