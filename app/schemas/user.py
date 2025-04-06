from pydantic import BaseModel, Field
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
    auth_method: Optional[str] = Field(default='telegram')

    class Config:
        from_attributes = True


class TelegramUserResponse(BaseUserResponse):
    id: int
    telegram_id: int
    username: str
    phone_number: str

    class Config:
        from_attributes = True


class GeneralUserResponse(BaseUserResponse):
    class Config:
        from_attributes = True