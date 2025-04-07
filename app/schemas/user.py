from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, TypeVar


UserCreateTypeVar = TypeVar('UserCreateTypeVar', bound='UserCreate')
UserResponseTypeVar = TypeVar('UserResponseTypeVar', bound='UserResponse')

class UserCreate(BaseModel):
    model_config = ConfigDict(extra='ignore', from_attributes=True)
    pass


class BaseUserResponse(BaseModel):
    model_config = ConfigDict(extra='ignore', from_attributes=True)
    pass


class TelegramUserCreate(UserCreate):
    telegram_id: int = Field(..., json_schema_extra=1)
    username: str = Field(..., json_schema_extra="@username")
    phone_number: Optional[str] = Field(..., json_schema_extra="+996700700700")
    auth_method: Optional[str] = Field(json_schema_extra='telegram')


class TelegramUserResponse(BaseUserResponse):
    id: int
    telegram_id: int
    username: str
    phone_number: str


class GeneralUserResponse(BaseUserResponse):
    pass
