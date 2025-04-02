from typing import Sequence

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.domain.models.trip import Trip
from app.domain.repositories.trip_repository import TripRepository


class SQLTripRepository(TripRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_trip(self, trip: Trip) -> Trip:
        self.session.add(trip)
        await self.session.commit()
        return trip

    async def cancel_trip(self, trip: Trip) -> Trip:
        await self.session.delete(trip)
        await self.session.commit()
        return trip

    async def get_trips(self) -> Sequence[Trip]:
        result = await self.session.execute(select(Trip))
        return result.scalars().all()
