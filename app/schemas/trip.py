from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class TripCreate(BaseModel):
    driver_id: int
    car_id: int
    origin: str = Field(..., max_length=255)
    start_lat: Optional[float] = None
    start_lon: Optional[float] = None
    destination: str = Field(..., max_length=255)
    end_lat: Optional[float] = None
    end_lon: Optional[float] = None
    start_time: datetime
    number_of_seats: int = Field(..., gt=0)

    class Config:
        from_attributes = True
