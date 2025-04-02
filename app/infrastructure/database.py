import warnings
from contextlib import asynccontextmanager
from typing import Any, AsyncGenerator

from app.core.config import database_settings
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, AsyncEngine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


engine: AsyncEngine = create_async_engine(
    url=database_settings.url,
    pool_recycle=900,
    pool_size=100,
    max_overflow=3,
)

SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


async def get_db() -> AsyncGenerator[Any, Any]:
    async with SessionLocal() as db:
        try:
            yield db
        except:
            warnings.warn("We somehow failed in a DB operation and auto-rollback")
            await db.rollback()
            raise


@asynccontextmanager
async def get_db_context() -> AsyncGenerator[Any, Any]:
    async with SessionLocal() as db:
        try:
            yield db
        except:
            warnings.warn("We somehow failed in a DB operation and auto-rollback")
            await db.rollback()
            raise
