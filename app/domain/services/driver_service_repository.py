from typing import Union, Any

from app.domain.models import Trip, Driver
from app.domain.repositories import DriverABCRepository
from app.schemas.driver import TelegramDriverCreate


class DriverService:

    __slots__ = ('__orm_repository',)

    def __init__(self, orm_repository: DriverABCRepository):
        self.__orm_repository = orm_repository

    async def create_driver(self, driver_data: dict[str, Any]) -> Driver:
        pass

    async def get_or_create_driver_by_user_id(self, driver_data: TelegramDriverCreate) -> Driver:
        driver = await self.__orm_repository.get_driver_by_user_id(driver_data.user_id)
        if driver is None:
            driver = await self.__orm_repository.create_driver(
                driver_data=driver_data.model_dump()
            )
        return driver
