from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.routers.tools.enums import APIStatusEnum
from app.domain.services.user_service import UserService
from app.domain.models import User
from app.infrastructure.database import get_db
from app.infrastructure.orm.user_repository import SQLUserRepository
from app.schemas.api_response import APIResponse
from app.schemas.user import TelegramUserCreate, TelegramUserResponse


router = APIRouter()


@router.post("/telegram_login/", response_model=APIResponse, tags=["Users"])
async def login_with_telegram(user_data: TelegramUserCreate, db: AsyncSession = Depends(get_db)):
    """
    **Authenticates a user.**
    - **telegram_id**: Unique Telegram ID
    - **username**: Unique Telegram Username
    - **phone_number**: Contact number
    - **Returns**: Created user data
    """
    user_repository = SQLUserRepository(db)
    user: User = await user_repository.get_user_by_telegram_id(telegram_id=user_data.telegram_id)
    if user is None:
        service = UserService(SQLUserRepository(db))
        user = await service.create_user(user_data=user_data)
    return APIResponse(
        status=APIStatusEnum.SUCCESS,
        message=f'User with telegram_id {user_data.username} authenticated successfully',
        detail=TelegramUserResponse.model_validate(user),
    )
