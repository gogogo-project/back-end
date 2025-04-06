from datetime import datetime, timedelta, timezone
from typing import Optional

from jwt import JWT
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from passlib.context import CryptContext

from app.core.config import security_settings
from app.error.jwt_error import ExpiredSignatureError, InvalidTokenError


SECRET_KEY = security_settings.JWT_SECRET_KEY
ALGORITHM = security_settings.JWT_ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = security_settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES
REFRESH_TOKEN_EXPIRE_DAYS = security_settings.JWT_REFRESH_TOKEN_EXPIRE_DAYS


jwt = JWT()


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


async def get_password_hash(password):
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, alg=ALGORITHM)
    return encoded_jwt


def create_refresh_token(data: dict):
    """Generate JWT Refresh Token"""
    expire = datetime.utcnow() + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    data.update({"exp": expire})
    return jwt.encode(data, SECRET_KEY, alg=ALGORITHM)


def verify_token(token: str):
    """Verify and Decode JWT Token"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        return payload
    except ExpiredSignatureError:
        return None  # Token has expired
    except InvalidTokenError:
        return None  # Invalid token
