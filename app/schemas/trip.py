from datetime import datetime
from typing import Optional

from pydantic import Field

from .base_schema import BaseCreate, BaseResponse


class TripDriverCreate(BaseCreate):
    driver_id: int = Field(..., json_schema_extra=1)
    car_model: str = Field(..., json_schema_extra="Audi A6")
    car_number: str = Field(..., json_schema_extra="NAA7776")
    number_of_seats: int = Field(..., json_schema_extra=4)

    origin: str = Field(..., json_schema_extra="Naryn")
    start_lat: Optional[float] = Field(..., json_schema_extra=41.42866)
    start_lon: Optional[float] = Field(..., json_schema_extra=75.99111)

    destination: str = Field(..., json_schema_extra="Bishkek")

    end_lat: Optional[float] = Field(..., json_schema_extra=42.87)
    end_lon: Optional[float] = Field(..., json_schema_extra=74.59)

    start_time: datetime = Field(..., json_schema_extra=datetime.now())
    end_time: datetime = Field(..., json_schema_extra=datetime.now())


class TripDriverResponse(BaseResponse):
    id: int
    driver_id: int
    car_model: str
    car_number: str
    number_of_seats: int
    origin: str
    start_lat: Optional[float]
    start_lon: Optional[float]
    destination: str
    end_lat: Optional[float]
    end_lon: Optional[float]
    start_time: datetime
    end_time: datetime
    created_at: datetime
    updated_at: datetime
