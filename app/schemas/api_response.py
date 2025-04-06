from typing import Any, Optional, Union

from app.api.routers.tools.enums import APIStatusEnum
from app.schemas.user import TelegramUserResponse, BaseModel


class APIResponse(BaseModel):
    status: Union[int, APIStatusEnum]
    message: Union[str, dict[str, Any]]
    detail: Optional[TelegramUserResponse]

    class Config:
        from_attributes = True