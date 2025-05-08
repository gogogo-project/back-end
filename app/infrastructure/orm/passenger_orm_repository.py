from typing import Union, Any, Optional

from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.orm import queries

from app.domain.repositories import PassengerABCRepository
from app.domain.models import Passenger, Trip



class PassengerORMRepository(PassengerABCRepository):

    __slots__ = ('__db',)

    def __init__(self, db: AsyncSession):
        self.__db = db

    async def create_passenger(self, passenger_data: dict[str, Any]) -> Passenger:
        passenger = Passenger(**passenger_data)
        self.__db.add(passenger)
        await self.__db.commit()
        await self.__db.refresh(passenger)
        return passenger

    async def update_passenger(self, passenger_data: dict[str, Any]) -> Union[Passenger, None]:
        async with self.__db as session:
            passenger: Optional[Passenger] = await queries.get_passenger_by_id(
                session,
                passenger_data['id'],
            )
            if passenger is None:
                return None
            for key, value in passenger_data.items():
                if hasattr(passenger, key):
                    setattr(passenger, key, value)
            session.add(passenger)
            await session.commit()
        return passenger

    async def delete_passenger(self, passenger_id: int) -> Union[Passenger, None]:
        async with self.__db as session:
            user = await queries.get_passenger_by_id(
                session=session,
                passenger_id=passenger_id,
            )
            if user:
                await self.__db.delete(user)
                await self.__db.commit()
        return user

    async def get_passenger_by_id(self, passenger_id: int) -> Union[Passenger, None]:
        async with self.__db as session:
            passenger: Optional[Passenger] = await queries.get_passenger_by_id(
                session=session,
                passenger_id=passenger_id,
            )
        return passenger

    async def get_passenger_by_user_id(self, user_id: int) -> Union[Passenger, None]:
        async with self.__db as session:
            passenger: Optional[Passenger] = await queries.get_passenger_by_user_id(
                session=session,
                user_id=user_id,
            )
        return passenger

    async def get_passenger_by_telegram_id(self, telegram_id: int) -> Union[Passenger, None]:
        pass

    async def get_trips(self, passenger_id: int) -> Union[None, list[Trip]]:
        async with self.__db as session:
            trips: Optional[list[Trip]] = await queries.get_trips(
                session=session,
                passenger_id=passenger_id,
            )
        return trips
