from __future__ import annotations

from typing import TYPE_CHECKING, Any, TypeVar

from aiogram import BaseMiddleware

if TYPE_CHECKING:
    from collections.abc import Awaitable, Callable

    from aiogram.types import TelegramObject

T = TypeVar("T")


class DependencyMiddleware(BaseMiddleware):
    def __init__(
        self,
        dependencies: dict[str, Any],
    ) -> None:
        self.dependencies = dependencies

    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> T | None:
        data.update(self.dependencies)

        return await handler(event, data)
