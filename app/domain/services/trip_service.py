from typing import Union

from app.domain.models import Trip
from app.domain.repositories.trip_repository import TripABCRepository
from app.schemas import TripCreate


class TripService:
    def __init__(self, repository: TripABCRepository):
        self.__repository = repository

    @staticmethod
    def normalize(string: str) -> str:
        string = ''.join(filter(str.isalpha, string.strip().lower()))
        return string

    async def create_ride(self, trip_data: TripCreate) -> Trip:
        trip_data = trip_data.model_dump()
        origin = self.normalize(trip_data['origin'])
        destination = self.normalize(trip_data['destination'])
        trip_data["origin_stipped"] = origin
        trip_data["destination_stipped"]= destination
        return await self.__repository.create_trip(trip_data=trip_data)

    async def cancel_ride(self, trip_id: int) -> Union[Trip, None]:
        return await self.__repository.cancel_trip(trip_id=trip_id)
