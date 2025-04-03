from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.routers.tools.enums import APIStatusEnum
from app.domain.services.user_service import UserService
from app.infrastructure.database import get_db
from app.infrastructure.orm.user_repository import SQLUserRepository
from app.schemas.api_response import APIResponse
from app.schemas.user import UserCreate, UserResponse



router = APIRouter()


@router.post(path="/telegram_create_user/", response_model=APIResponse, tags=["Users"])
async def create_user_with_telegram(user: UserCreate, db: AsyncSession = Depends(get_db)):
    """
    **Creates a new user.**
    - **telegram_id**: Unique Telegram ID
    - **name**: Full name
    - **phone_number**: Contact number
    - **Returns**: Created user data
    """
    user_repository = SQLUserRepository(db)
    existing_user = await user_repository.is_user_exists(telegram_id=user.telegram_id)
    if existing_user:
        return APIResponse(
            status=APIStatusEnum.ALREADY_EXISTS,
            message=f'User with telegram_id {user.telegram_id} already exists',
            detail={}
        )
    service = UserService(SQLUserRepository(db))
    new_user = await service.create_user(user)
    return APIResponse(
        status=APIStatusEnum.CREATED,
        message=f'User with telegram_id {new_user.telegram_id} created',
        detail=UserResponse.model_validate(new_user)
    )
