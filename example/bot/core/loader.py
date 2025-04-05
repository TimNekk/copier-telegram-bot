from __future__ import annotations

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.base import DefaultKeyBuilder
from aiogram.fsm.storage.redis import RedisStorage
from redis.asyncio import ConnectionPool, Redis

from bot.core.settings import Settings
from bot.database.database import get_sessionmaker

settings = Settings()

bot = Bot(
    token=settings.bot.token.get_secret_value(),
    default=DefaultBotProperties(
        parse_mode=ParseMode.HTML,
        link_preview_is_disabled=True,
    ),
)

redis_client = Redis(
    connection_pool=ConnectionPool(
        host="redis",
        port=settings.redis.port,
        db=0,
    ),
)

storage = RedisStorage(
    redis=redis_client,
    key_builder=DefaultKeyBuilder(
        with_destiny=True,
    ),
)

dp = Dispatcher(
    storage=storage,
)

sessionmaker = get_sessionmaker(url=settings.postgres.url.get_secret_value())
