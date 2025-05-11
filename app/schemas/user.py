from pydantic import Field
from typing import Optional

from .base_schema import BaseUserCreate, BaseUserResponse


class TelegramUserCreate(BaseUserCreate):
    telegram_id: int = Field(..., json_schema_extra=1)
    name: str = Field(..., json_schema_extra='Elnazar')
    username: str = Field(..., json_schema_extra="@username")
    phone_number: Optional[str] = Field(..., json_schema_extra="+996700700700")
    auth_method: Optional[str] = Field(json_schema_extra='telegram')


class TelegramUserResponse(BaseUserResponse):
    id: int
    telegram_id: int
    name: str
    username: str
    phone_number: str


class GeneralUserResponse(BaseUserResponse):
    pass
