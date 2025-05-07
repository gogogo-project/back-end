from typing import Union, Any, Optional

from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.orm import queries

from app.domain.repositories import DriverABCRepository
from app.domain.models import Driver, Trip



class DriverORMRepository(DriverABCRepository):

    __slots__ = ('__db',)

    def __init__(self, db: AsyncSession):
        self.__db = db

    async def create_driver(self, driver_data: dict[str, Any]) -> Driver:
        driver = Driver(**driver_data)
        self.__db.add(driver)
        await self.__db.commit()
        await self.__db.refresh(driver)
        return driver

    async def update_driver(self, driver_data: dict[str, Any]) -> Union[Driver, None]:
        async with self.__db as session:
            driver: Optional[Driver] = await queries.get_driver_by_id(
                session,
                driver_data['id'],
            )
            if driver is None:
                return None
            for key, value in driver_data.items():
                if hasattr(driver, key):
                    setattr(driver, key, value)
            session.add(driver)
            await session.commit()
        return driver

    async def delete_driver(self, driver_id: int) -> Union[Driver, None]:
        async with self.__db as session:
            user = await queries.get_driver_by_id(
                session=session,
                driver_id=driver_id,
            )
            if user:
                await self.__db.delete(user)
                await self.__db.commit()
        return user

    async def get_driver_by_id(self, driver_id: int) -> Union[Driver, None]:
        async with self.__db as session:
            driver: Optional[Driver] = await queries.get_driver_by_id(
                session=session,
                driver_id=driver_id,
            )
        return driver

    async def get_driver_by_user_id(self, user_id: int) -> Union[Driver, None]:
        async with self.__db as session:
            driver: Optional[Driver] = await queries.get_driver_by_user_id(
                session=session,
                user_id=user_id,
            )
        return driver

    async def get_driver_by_telegram_id(self, telegram_id: int) -> Union[Driver, None]:
        pass

    async def get_trips(self, driver_id: int) -> Union[None, list[Trip]]:
        async with self.__db as session:
            trips: Optional[list[Trip]] = await queries.get_trips(
                session=session,
                driver_id=driver_id,
            )
        return trips
