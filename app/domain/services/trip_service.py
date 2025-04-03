from app.domain.models import Trip
from app.domain.repositories.trip_repository import TripRepository

class TripService:
    def __init__(self, repository: TripRepository):
        self.repository = repository

    async def create_ride(self, trip_data: dict) -> Trip:
        trip = Trip(**trip_data)
        return await self.repository.create_trip(trip=trip)

    async def cancel_ride(self, trip: Trip) -> Trip:
        return await self.repository.cancel_trip(trip=trip)
