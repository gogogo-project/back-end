from abc import ABC, abstractmethod
from app.domain.models.trip import Trip


class TripRepository(ABC):
    @abstractmethod
    async def create_trip(self, trip: Trip) -> Trip:
        pass

    @abstractmethod
    async def cancel_trip(self, trip: Trip) -> Trip:
        pass

    @abstractmethod
    async def get_trips(self) -> list[Trip]:
        pass
