from typing import TypeVar

from pydantic import BaseModel, ConfigDict


UserCreateTypeVar = TypeVar('UserCreateTypeVar', bound='BaseUserCreate')
UserResponseTypeVar = TypeVar('UserResponseTypeVar', bound='BaseUserResponse')


class BaseUserCreate(BaseModel):
    model_config = ConfigDict(extra='ignore', from_attributes=True)


class BaseUserResponse(BaseModel):
    model_config = ConfigDict(extra='ignore', from_attributes=True)
