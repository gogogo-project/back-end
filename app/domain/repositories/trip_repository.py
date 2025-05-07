from typing import Any, Union

from abc import ABC, abstractmethod
from app.domain.models import Trip


class TripABCRepository(ABC):
    @abstractmethod
    async def create_trip(self, trip_data: dict[str, Any]) -> Trip:
        pass

    @abstractmethod
    async def cancel_trip(self, trip_id: int) -> Union[Trip, None]:
        pass
