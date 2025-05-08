from typing import Any, Union

from abc import ABC, abstractmethod
from app.domain.models import Passenger, Trip


class PassengerABCRepository(ABC):

    @abstractmethod
    async def create_passenger(
            self,
            passenger_data: dict[str, Any],
    ) -> Passenger:
        pass

    @abstractmethod
    async def update_passenger(
            self,
            passenger_data: dict[str, Any],
    ) -> Union[Passenger, None]:
        pass

    @abstractmethod
    async def delete_passenger(
            self,
            passenger_id: int,
    ) -> Union[Passenger, None]:
        pass

    @abstractmethod
    async def get_passenger_by_id(
            self,
            passenger_id: int,
    ) -> Union[Passenger, None]:
        pass

    @abstractmethod
    async def get_passenger_by_user_id(
            self,
            user_id: int,
    ) -> Union[Passenger, None]:
        pass

    @abstractmethod
    async def get_passenger_by_telegram_id(
            self,
            telegram_id: int,
    ) -> Union[Passenger, None]:
        pass

    @abstractmethod
    async def get_trips(self, passenger_id: int) -> Union[list[Trip], None]:
        pass
