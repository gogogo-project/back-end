from typing import Optional, Union

from app.domain.models import Passenger
from app.domain.repositories import PassengerABCRepository
from app.schemas import TelegramPassengerCreate


class PassengerService:
    __slots__ = ('__passenger_orm',)
    def __init__(self, passenger_orm: PassengerABCRepository) -> None:
        self.__passenger_orm = passenger_orm

    async def create_or_get_passenger(self, passenger_data: TelegramPassengerCreate) -> Passenger:
        passenger: Optional[Passenger] = await self.__passenger_orm.get_passenger_by_user_id(
            user_id=passenger_data.user_id,
        )
        if passenger is None:
            passenger: Optional[Passenger] = await self.__passenger_orm.create(passenger_data=passenger_data)

        return passenger

    async def get_passenger_by_user_id(self, user_id: int) -> Union[Passenger, None]:
        passenger: Optional[Passenger] = await self.__passenger_orm.get_passenger_by_user_id(user_id=user_id)
        return passenger
