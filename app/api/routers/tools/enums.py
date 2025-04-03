from enum import Enum


class APIStatusEnum(Enum):
    SUCCESS: int = 200
    CREATED: int = 201
    ACCEPTED: int = 202
    NOT_FOUND: int = 404
    ALREADY_EXISTS: int = 409
