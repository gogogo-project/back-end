from typing import Union, Any

from app.domain.models import Trip, Passenger
from app.domain.repositories import PassengerABCRepository
from app.schemas.passenger import TelegramPassengerCreate


class PassengerService:

    __slots__ = ('__orm_repository',)

    def __init__(self, orm_repository: PassengerABCRepository):
        self.__orm_repository = orm_repository

    async def create_passenger(self, passenger_data: dict[str, Any]) -> Passenger:
        pass

    async def get_or_create_passenger_by_user_id(self, passenger_data: TelegramPassengerCreate) -> Passenger:
        passenger = await self.__orm_repository.get_passenger_by_user_id(passenger_data.user_id)
        if passenger is None:
            passenger = await self.__orm_repository.create_passenger(
                passenger_data=passenger_data.model_dump()
            )
        return passenger
