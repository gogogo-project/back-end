from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.routers.tools.enums import APIStatusEnum
from app.domain.services import UserService, DriverService, PassengerService
from app.domain.models import User, Driver, Passenger
from app.infrastructure.database import get_db
from app.infrastructure.orm import (
    UserORMRepository,
    DriverORMRepository,
    PassengerORMRepository
)
from app.schemas import (
    APIResponse,
    TelegramUserCreate,
    TelegramUserResponse,
    TelegramDriverCreate,
    TelegramDriverResponse,
    TelegramPassengerCreate,
    TelegramPassengerResponse,
)


router = APIRouter()


@router.post(path="/telegram_user/", response_model=APIResponse, tags=["Users"])
async def telegram_user(user_data: TelegramUserCreate, db: AsyncSession = Depends(get_db)):
    user_service = UserService(UserORMRepository(db))
    user: User = await user_service.get_or_create_user(
        user_data=user_data,
    )

    return APIResponse(
        status=APIStatusEnum.SUCCESS,
        message=f'User with telegram_id {user.username} authenticated successfully',
        detail=TelegramUserResponse.model_validate(user),
    )


@router.post(path="/telegram_driver/", response_model=APIResponse, tags=["Users"])
async def telegram_driver(driver_data: TelegramDriverCreate, db: AsyncSession = Depends(get_db)):
    driver_service = DriverService(DriverORMRepository(db))
    driver: Driver = await driver_service.get_or_create_driver_by_user_id(
        driver_data=driver_data,
    )

    return APIResponse(
        status=APIStatusEnum.SUCCESS,
        message=f'Driver with telegram_id {driver.user_id} authenticated successfully',
        detail=TelegramDriverResponse.model_validate(driver),
    )


@router.post(path="/telegram_passenger/", response_model=APIResponse, tags=["Users"])
async def telegram_passenger(passenger_data: TelegramPassengerCreate, db: AsyncSession = Depends(get_db)):
    passenger_service = PassengerService(PassengerORMRepository(db))
    passenger: Passenger = await passenger_service.get_or_create_passenger_by_user_id(
        passenger_data=passenger_data,
    )

    return APIResponse(
        status=APIStatusEnum.SUCCESS,
        message=f'Driver with telegram_id {passenger.user_id} authenticated successfully',
        detail=TelegramDriverResponse.model_validate(passenger),
    )
