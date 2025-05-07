from typing import Any, Union

from abc import ABC, abstractmethod
from app.domain.models import Driver, Trip


class DriverABCRepository(ABC):

    @abstractmethod
    async def create_driver(
            self,
            driver_data: dict[str, Any],
    ) -> Driver:
        pass

    @abstractmethod
    async def update_driver(
            self,
            driver_data: dict[str, Any],
    ) -> Union[Driver, None]:
        pass

    @abstractmethod
    async def delete_driver(
            self,
            driver_id: int,
    ) -> Union[Driver, None]:
        pass

    @abstractmethod
    async def get_driver_by_id(
            self,
            driver_id: int,
    ) -> Union[Driver, None]:
        pass

    @abstractmethod
    async def get_driver_by_user_id(
            self,
            user_id: int,
    ) -> Union[Driver, None]:
        pass

    @abstractmethod
    async def get_driver_by_telegram_id(
            self,
            telegram_id: int,
    ) -> Union[Driver, None]:
        pass

    @abstractmethod
    async def get_trips(self, driver_id: int) -> Union[list[Trip], None]:
        pass
