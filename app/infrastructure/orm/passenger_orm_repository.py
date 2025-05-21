from typing import Union, Any, Optional

from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.orm import queries

from app.domain.repositories import PassengerABCRepository
from app.domain.models import Passenger
from app.schemas import TelegramPassengerCreate


class PassengerORMRepository(PassengerABCRepository):

    __slots__ = ('__db',)

    def __init__(self, db: AsyncSession):
        self.__db = db

    async def create(self, passenger_data: TelegramPassengerCreate) -> Union[Passenger, None]:
        async with self.__db as session:
            passenger = Passenger(**passenger_data.model_dump())
            session.add(passenger)
            await session.commit()
            await session.refresh(passenger)
        return passenger

    async def get_passenger_by_user_id(self, user_id: int) -> Union[Passenger, None]:
        async with self.__db as session:
            passenger: Optional[Passenger] = await queries.get_passenger_by_user_id(
                session=session,
                user_id=user_id,
            )
        return passenger
