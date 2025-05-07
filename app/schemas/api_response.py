from typing import Any, Optional, Union, Generic, TypeVar

from pydantic import BaseModel, ConfigDict

from app.api.routers.tools.enums import APIStatusEnum


T = TypeVar('T')

class APIResponse(BaseModel, Generic[T]):
    status: Union[int, APIStatusEnum]
    message: Union[str, dict[str, Any]]
    detail: Optional[T]

    model_config = ConfigDict(extra='ignore', from_attributes=True)
