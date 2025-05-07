from abc import ABC, abstractmethod

from app.schemas.base_schema import UserCreateTypeVar, UserResponseTypeVar
from app.domain.repositories.user_repository import UserABCRepository

class BaseUserCreationStrategy(ABC):
    """
    Abstract base class for different user creation strategies.
    """
    @abstractmethod
    async def create(self, user_data: UserCreateTypeVar, repository: UserABCRepository) -> UserResponseTypeVar:
        pass
