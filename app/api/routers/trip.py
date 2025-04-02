from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.infrastructure.database import get_db
from app.infrastructure.orm.trip_repository import SQLTripRepository
from app.domain.services.trip_service import TripService
from app.schemas.trip import TripCreate

router = APIRouter()

@router.post("/rides/")
async def create_ride(ride: TripCreate, db: AsyncSession = Depends(get_db)):
    service = TripService(SQLTripRepository(db))
    new_ride = await service.create_ride(ride.dict())
    return {"message": "Ride created", "ride": new_ride}
