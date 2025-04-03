from app.domain.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate, UserResponse


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def create_user(self, user_data: UserCreate) -> UserResponse:
        existing_user = await self.user_repository.is_user_exists(telegram_id=user_data.telegram_id)
        if existing_user:
            raise ValueError("User with this Telegram ID already exists.")

        user = await self.user_repository.create_user(user_data.dict())
        return UserResponse(
            id=user.id,
            telegram_id=user.telegram_id,
            name=user.name,
            phone_number=user.phone_number,
            is_blocked=user.is_blocked,
            blocked_at=user.blocked_at,
        )
