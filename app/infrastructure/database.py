import warnings
from contextlib import asynccontextmanager
from typing import Any, AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from app.core.config import database_settings


Base = declarative_base()

DATABASE_URL = database_settings.url
engine = create_async_engine(DATABASE_URL, pool_recycle=900, pool_size=100, max_overflow=3)

async_session_maker = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


@asynccontextmanager
async def get_db_context() -> AsyncGenerator[Any, Any]:
    async with async_session_maker() as db:
        try:
            yield db
        except:
            warnings.warn("We somehow failed in a DB operation and auto-rollback")
            await db.rollback()
            raise

async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
