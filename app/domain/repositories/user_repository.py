from abc import ABC, abstractmethod
from app.domain.models.user import User, Passenger, Driver


class UserRepository(ABC):
    @abstractmethod
    async def create_user(self, user: User) -> User:
        pass

    @abstractmethod
    async def get_user(self, user_id: int) -> User:
        pass

    @abstractmethod
    async def delete_user(self, user_id: int) -> User:
        pass

