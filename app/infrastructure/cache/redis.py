from redis import asyncio

from app.core.config import redis_settings


token_blocklist = asyncio.from_url(redis_settings.url)


async def add_jti_to_blocklist(jti: str) -> None:
    await token_blocklist.set(name=jti, value="", ex=redis_settings.REDIS_JTI_EXPIRY)


async def token_in_blocklist(jti: str) -> bool:
    jti = await token_blocklist.get(jti)

    return jti is not None
