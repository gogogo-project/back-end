from pydantic import BaseModel
from typing import Any, Optional

from app.api.routers.tools.enums import APIStatusEnum


class APIResponse(BaseModel):
    status: APIStatusEnum
    message: str | dict[str, Any]
    detail: Optional[Any] = None

    class Config:
        from_attributes = True
