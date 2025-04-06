from pydantic import BaseModel, Field, field_validator
from typing import Optional, Final, TypeVar


UserCreateTypeVar = TypeVar('UserCreateTypeVar', bound='UserCreate')
UserResponseTypeVar = TypeVar('UserResponseTypeVar', bound='UserResponse')

class UserCreate(BaseModel):
    pass


class BaseUserResponse(BaseModel):
    pass


class TelegramUserCreate(UserCreate):
    telegram_id: int = Field(..., example=1)
    username: str = Field(..., example="@username")
    phone_number: Optional[str] = Field(..., example="+996700700700")
    auth_method: Final[str] = 'telegram'

    class Config:
        from_attributes = True


class TelegramUserResponse(BaseUserResponse):
    id: int
    telegram_id: int
    username: str
    phone_number: str

    class Config:
        from_attributes = True

    @field_validator('telegram_id')
    def validate_phone_number(cls, value):
        return int(value)


class GeneralUserResponse(BaseUserResponse):
    class Config:
        from_attributes = True