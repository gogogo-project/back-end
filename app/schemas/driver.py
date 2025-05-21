from pydantic import Field

from .base_schema import BaseCreate, BaseResponse


class TelegramDriverCreate(BaseCreate):
    user_id: int = Field(..., json_schema_extra="@username")


class TelegramDriverResponse(BaseResponse):
    id: int
    user_id: int


class GeneralDriverResponse(BaseResponse):
    pass
