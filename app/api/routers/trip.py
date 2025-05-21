from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.database import get_db
from app.infrastructure.orm import TripORMRepository
from app.domain.services import TripService
from app.domain.models import Trip
from app.schemas import (
    APIResponse,
    TripDriverCreate,
    TripDriverResponse,
)


router = APIRouter()


@router.post("/telegram_create_trip/", response_model=APIResponse, tags=["Trips"])
async def telegram_create_trip(trip_data: TripDriverCreate, db: AsyncSession = Depends(get_db)):
    trip_service = TripService(TripORMRepository(db))
    trip: Trip = await trip_service.create_ride(trip_data)

    return APIResponse(
        status=201,
        message='Trip created successfully',
        detail=TripDriverResponse.model_validate(trip)
    )
