from __future__ import annotations

from typing import TYPE_CHECKING, Any, TypeVar

from aiogram import BaseMiddleware
from aiogram.types import Message
from cachetools import TTLCache

if TYPE_CHECKING:
    from collections.abc import Awaitable, Callable

    from bot.core.settings import Settings

T = TypeVar("T")


class ThrottlingMiddleware(BaseMiddleware):
    def __init__(self) -> None:
        self.cache = None

    async def __call__(
        self,
        handler: Callable[[Message, dict[str, Any]], Awaitable[T]],
        event: Message,
        data: dict[str, Any],
    ) -> T | None:
        if not isinstance(event, Message):  # TODO(donBarbos): add support CallbackQuery or Update
            return await handler(event, data)

        if self.cache is None:
            settings: Settings = data["settings"]
            rate_limit = settings.bot.rate_limit
            self.cache = TTLCache(maxsize=10_000, ttl=rate_limit)

        if event.chat.id in self.cache:
            return None
        self.cache[event.chat.id] = None
        return await handler(event, data)
