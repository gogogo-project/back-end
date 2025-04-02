from app.domain.models.user import User
from app.domain.repositories.user_repository import UserRepository

class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def create_user(self, user_data: dict) -> User:
        user = User(**user_data)
        return await self.repository.create_user(user)

    async def delete_user(self, user_id: int) -> User:
        user = await self.repository.get_user(user_id)
        return await self.repository.delete_user(user)
