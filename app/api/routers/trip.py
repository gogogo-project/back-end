from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.database import get_db
from app.infrastructure.orm import TripORMRepository
from app.domain.services import TripService
from app.domain.models import Trip
from app.schemas import (
    APIResponse,
    TripCreate,
    TripResponse,
)


router = APIRouter()


@router.post("/telegram_trip_create/", response_model=APIResponse, tags=["Trips"])
async def telegram_create_driver(trip_data: TripCreate, db: AsyncSession = Depends(get_db)):
    trip_service = TripService(TripORMRepository(db))
    trip: Trip = await trip_service.create_ride(trip_data)

    print(f'{trip=}')

    return APIResponse(
        status=201,
        message='Trip created successfully',
        detail=TripResponse.model_validate(trip)
    )
