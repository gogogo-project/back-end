from typing import Optional


class ExpiredSignatureError(Exception):
    def __init__(self, message: Optional[str] = None) -> None:
        if message is None:
            message = 'Expired Signature'
        super().__init__(message)


class InvalidTokenError(Exception):
    def __init__(self, message: Optional[str] = None) -> None:
        if message is None:
            message = 'Invalid Token'
        super().__init__(message)
