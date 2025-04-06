from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.routers.tools.enums import APIStatusEnum
from app.domain.services.user_service import UserService
from app.domain.models import User
from app.infrastructure.database import get_db
from app.infrastructure.orm.user_repository import SQLUserRepository
from app.schemas.api_response import APIResponse
from app.schemas.user import BaseUserResponse, TelegramUserCreate, TelegramUserResponse



router = APIRouter()


@router.post("/telegram_login/", response_model=TelegramUserResponse, tags=["Users"])
async def login_with_telegram(user_data: TelegramUserCreate, db: AsyncSession = Depends(get_db)):
    user_repository = SQLUserRepository(db)
    user: User = await user_repository.get_user_by_telegram_id(telegram_id=user_data.telegram_id)
    if user is None:
        service = UserService(SQLUserRepository(db))
        user: TelegramUserResponse = await service.create_user(user_data=user_data)
        return APIResponse(
            status=APIStatusEnum.CREATED,
            message=f'User with telegram_id {user_data.username} authenticated successfully',
            detail=user,
        )
    detail = TelegramUserResponse.model_validate(user)
    return APIResponse(
        status=APIStatusEnum.SUCCESS,
        message=f'User with telegram_id {user_data.username} authenticated successfully',
        detail=TelegramUserResponse(
            id=user.id,
            telegram_id=user.telegram_id,
            username=user.username,
            phone_number=user.phone_number,

        ),
    ).model_dump()



# @router.post(path="/telegram_create_user/", response_model=APIResponse, tags=["Users"])
# async def create_user_with_telegram(user: UserCreate, db: AsyncSession = Depends(get_db)):
#     """
#     **Creates a new user.**
#     - **telegram_id**: Unique Telegram ID
#     - **name**: Full name
#     - **phone_number**: Contact number
#     - **Returns**: Created user data
#     """
#     user_repository = SQLUserRepository(db)
#     existing_user = await user_repository.is_user_exists(telegram_id=user.telegram_id)
#     if existing_user:
#         return APIResponse(
#             status=APIStatusEnum.ALREADY_EXISTS,
#             message=f'User with telegram_id {user.telegram_id} already exists',
#             detail={}
#         )
#     service = UserService(SQLUserRepository(db))
#     new_user = await service.create_user(user)
#     return APIResponse(
#         status=APIStatusEnum.CREATED,
#         message=f'User with telegram_id {new_user.telegram_id} created',
#         detail=UserResponse.model_validate(new_user)
#     )
