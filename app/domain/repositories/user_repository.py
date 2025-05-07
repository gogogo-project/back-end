from abc import ABC, abstractmethod

from app.domain.models import User


class UserABCRepository(ABC):
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
    async def is_user_exists(self, **kwargs) -> bool:
        pass

    @abstractmethod
    async def get_user_by_auth_method(self, auth_method: str, identifier: str | int) -> bool:
        pass
