from abc import ABC, abstractmethod

from app.schemas.user import UserCreate, UserResponse
from app.domain.repositories.user_repository import UserRepository

class BaseUserCreationStrategy(ABC):
    """
    Abstract base class for different user creation strategies.
    """
    @abstractmethod
    async def create(self, user_data: UserCreate, repository: UserRepository) -> UserResponse:
        pass
