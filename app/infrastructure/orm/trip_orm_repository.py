from typing import Sequence, Any, Union, Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.domain.models import Trip
from app.domain.repositories.trip_repository import TripABCRepository


class TripORMRepository(TripABCRepository):
    def __init__(self, db: AsyncSession):
        self.__db = db

    async def create_trip(self, trip_data: dict[str, Any]) -> Trip:
        async with self.__db as session:
            trip = Trip(**trip_data)
            self.__db.add(trip)
            await session.commit()
            await session.refresh(trip)
        return trip

    async def cancel_trip(self, trip_id: int) -> Union[Trip, None]:
        async with self.__db as session:
            trip: Optional[Trip] = (
                await session.execute(
                    select(Trip).where(
                        Trip.id == trip_id
                    )
                )
            ).scalar_one_or_none()

            if trip is None:
                return None
            await session.delete(trip)
            await session.commit()

        return trip
