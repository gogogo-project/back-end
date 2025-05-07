from typing import Type, Optional

from app.core.security import get_password_hash
from app.domain.models import User
from app.domain.repositories.user_repository import UserABCRepository
from app.error.user_errors import ValidationException, UserAlreadyExistsException
from app.schemas import (
    TelegramUserResponse,
    TelegramUserCreate,
    GeneralUserResponse,
)
from app.schemas.base_schema import (
    UserCreateTypeVar,
    UserResponseTypeVar,
)

from app.domain.services.bases import BaseUserCreationStrategy


class TelegramUserCreationStrategy(BaseUserCreationStrategy):
    """
    Handles Telegram-based user creation.
    """
    async def create(self, user_data: UserCreateTypeVar, repository: UserABCRepository):
        if not user_data.telegram_id:
            raise ValidationException("Telegram ID is required for Telegram authentication.")

        return await repository.create_user(user_data)


class EmailUserCreationStrategy(BaseUserCreationStrategy):
    """
    Handles Email-based user creation.
    """
    async def create(self, user_data: UserCreateTypeVar, repository: UserABCRepository):
        if not user_data.email or not user_data.password:
            raise ValidationException("Email and password are required for email authentication.")

        user_data.password = get_password_hash(user_data.password)
        return await repository.create_user(user_data.model_dump())


class PhoneUserCreationStrategy(BaseUserCreationStrategy):
    """
    Handles Phone-based user creation.
    """
    async def create(self, user_data: UserCreateTypeVar, repository: UserABCRepository):
        if not user_data.phone_number:
            raise ValidationException("Phone number is required for phone authentication.")

        return await repository.create_user(user_data.model_dump())


class UserService:
    strategies: dict[str, Type[BaseUserCreationStrategy]] = {
        "telegram": TelegramUserCreationStrategy(),
        "email": EmailUserCreationStrategy(),
        "phone": PhoneUserCreationStrategy(),
    }
    def __init__(self, user_repository: UserABCRepository):
        self.user_repository = user_repository

    async def get_or_create_user(self, user_data: TelegramUserCreate) -> User:
        user: Optional[User] = await self.user_repository.get_user_by_telegram_id(
            telegram_id=user_data.telegram_id
        )
        if user is None:
            user: Optional[User] = await self.user_repository.create_user(user_data=user_data.model_dump())
        return user

    async def create_user(self, user_data: UserCreateTypeVar) -> UserResponseTypeVar:
        """
               Main user creation method. Selects the appropriate strategy based on `auth_method`.
               """
        auth_method = user_data.auth_method
        if auth_method == 'telegram':
            identifier = user_data.telegram_id
        else:
            identifier = user_data.email or user_data.phone_number
        if auth_method not in self.strategies:
            raise ValidationException(f"Unsupported authentication method: {user_data.auth_method}")

        if identifier is None:
            raise ValidationException("Identifier must be provided")

        existing_user = await self.user_repository.get_user_by_auth_method(
            auth_method=auth_method,
            identifier=identifier
        )
        if existing_user:
            raise UserAlreadyExistsException("User already exists with this identifier.")

        strategy = self.strategies[user_data.auth_method]
        user = await strategy.create(user_data=user_data, repository=self.user_repository)
        if auth_method == "telegram":
            return TelegramUserResponse.model_validate(user)
        return GeneralUserResponse.model_validate(user)