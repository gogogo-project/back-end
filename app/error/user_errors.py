from typing import Optional


class ValidationException(Exception):
    def __init__(self, message: Optional[str] = None) -> None:
        if message is None:
            message = "Invalid authentication."
        super().__init__(message)


class UserAlreadyExistsException(Exception):
    def __init__(self, message: Optional[str] = None) -> None:
        if message is None:
            message = "User already exists."
        super().__init__(message)
