from pydantic import Field

from .base_schema import BaseCreate, BaseResponse


class TelegramPassengerCreate(BaseCreate):
    user_id: int = Field(..., json_schema_extra="@username")
    person_to_notify: str = Field(..., json_schema_extra="@username")


class TelegramPassengerResponse(BaseResponse):
    id: int
    user_id: int
    person_to_notify: str


class GeneralPassengerResponse(BaseResponse):
    pass
