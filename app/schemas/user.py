from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime


class UserCreate(BaseModel):
    telegram_id: Optional[int] = Field(None, example="1")
    username: Optional[str] = Field(None, example="john_doe")
    email: Optional[EmailStr] = Field(None, example="user@example.com")
    phone_number: Optional[str] = Field(None, example="+123456789")
    password: Optional[str] = Field(None, example="securepassword123")
    auth_method: str = Field(..., example="telegram")  # Required to specify the method

    class Config:
        from_attributes = True


class UserResponse(BaseModel):
    id: int
    username: Optional[str]
    telegram_id: Optional[int] = None
    email: Optional[EmailStr] = None
    phone_number: Optional[str] = None
    is_blocked: Optional[bool] = None
    blocked_at: Optional[datetime] = None

    class Config:
        from_attributes = True
