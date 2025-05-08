from pydantic import Field
from typing import Optional

from .base_schema import BaseUserCreate, BaseUserResponse


class TelegramPassengerCreate(BaseUserCreate):
    user_id: int = Field(..., json_schema_extra="@username")


class TelegramPassengerResponse(BaseUserResponse):
    id: int
    user_id: int


class GeneralPassengerResponse(BaseUserResponse):
    pass
