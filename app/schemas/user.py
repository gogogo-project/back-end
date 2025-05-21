from pydantic import Field
from typing import Optional

from .base_schema import BaseCreate, BaseResponse


class TelegramUserCreate(BaseCreate):
    telegram_id: int = Field(..., json_schema_extra=1)
    name: str = Field(..., json_schema_extra='Elnazar')
    username: str = Field(..., json_schema_extra="@username")
    phone_number: Optional[str] = Field(..., json_schema_extra="+996700700700")
    auth_method: Optional[str] = Field(json_schema_extra='telegram')


class TelegramUserResponse(BaseResponse):
    id: int
    telegram_id: int
    name: str
    username: str
    phone_number: str


class GeneralUserResponse(BaseResponse):
    pass
