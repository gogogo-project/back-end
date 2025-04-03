from pydantic import SecretStr
from pydantic_settings import BaseSettings as _BaseSettings, SettingsConfigDict
from sqlalchemy.engine import URL

from utils import get_environment_file_path


class BaseSettings(_BaseSettings):
    model_config = SettingsConfigDict(
        env_file=get_environment_file_path(),
        env_file_encoding="utf-8",
        extra="ignore",
    )


class SecuritySettings(BaseSettings):
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int


class DatabaseSettings(BaseSettings):
    POSTGRES_HOST: str
    POSTGRES_PASSWORD: SecretStr
    POSTGRES_DB: str
    POSTGRES_PORT: int
    POSTGRES_USER: str

    @property
    def url(self) -> URL:
        url: URL = URL.create(
            drivername="postgresql+asyncpg",
            username=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD.get_secret_value(),
            host=self.POSTGRES_HOST,
            port=self.POSTGRES_PORT,
            database=self.POSTGRES_DB,
        )
        return url

class RedisSettings(BaseSettings):
    REDIS_HOST: str
    REDIS_PASSWORD: SecretStr
    REDIS_PORT: int
    REDIS_DB: int  # Should be an integer

    @property
    def url(self) -> str:
        return f"redis://:{self.REDIS_PASSWORD.get_secret_value()}@{self.REDIS_HOST}:{self.REDIS_PORT}/{self.REDIS_DB}"

settings = BaseSettings()
security_settings = SecuritySettings()
database_settings = DatabaseSettings()
redis_settings = RedisSettings()
