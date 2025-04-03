from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class UserCreate(BaseModel):
    telegram_id: str = Field(..., max_length=255)
    name: str = Field(..., max_length=255)
    phone_number: str = Field(..., max_length=255)


class UserResponse(BaseModel):
    id: int
    telegram_id: str
    name: str
    phone_number: str
    is_blocked: bool
    blocked_at: Optional[datetime]

    class Config:
        from_attributes = True
