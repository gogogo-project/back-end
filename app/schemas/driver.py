from pydantic import Field
from typing import Optional

from .base_schema import BaseUserCreate, BaseUserResponse


class TelegramDriverCreate(BaseUserCreate):
    user_id: int = Field(..., json_schema_extra={"example" : 1})


class TelegramDriverResponse(BaseUserResponse):
    id: int
    user_id: int


class GeneralDriverResponse(BaseUserResponse):
    pass
