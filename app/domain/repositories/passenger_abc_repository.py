from abc import ABC, abstractmethod
from typing import Union

from app.domain.models import Passenger
from app.schemas import TelegramPassengerCreate


class PassengerABCRepository(ABC):
    @abstractmethod
    async def create(self, passenger_data: TelegramPassengerCreate) -> Union[Passenger, None]:
        raise NotImplementedError

    @abstractmethod
    async def get_passenger_by_user_id(self, user_id: int) -> Union[Passenger, None]:
        raise NotImplementedError
