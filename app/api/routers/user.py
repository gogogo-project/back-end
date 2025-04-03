from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.infrastructure.database import get_db
from app.domain.services.user_service import UserService
from app.infrastructure.orm.user_repository import SQLUserRepository
from app.schemas.user import UserCreate, UserResponse


router = APIRouter()


@router.post("/users/", response_model=UserResponse, tags=["Users"])
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    """
    **Creates a new user.**
    - **telegram_id**: Unique Telegram ID
    - **name**: Full name
    - **phone_number**: Contact number
    - **Returns**: Created user data
    """
    user_repository = SQLUserRepository(db)
    existing_user = await user_repository.is_user_exists(telegram_id=user.telegram_id)
    print(True if existing_user else False)
    service = UserService(SQLUserRepository(db))
    new_user = await service.create_user(user)
    return new_user
