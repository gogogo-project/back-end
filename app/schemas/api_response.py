from typing import Any, Optional, Union

from pydantic import BaseModel, ConfigDict

from app.api.routers.tools.enums import APIStatusEnum
from app.schemas.user import TelegramUserResponse


class APIResponse(BaseModel):
    status: Union[int, APIStatusEnum]
    message: Union[str, dict[str, Any]]
    detail: Optional[TelegramUserResponse]

    model_config = ConfigDict(extra='ignore', from_attributes=True)
