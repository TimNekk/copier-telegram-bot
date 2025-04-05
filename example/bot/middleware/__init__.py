from __future__ import annotations

from typing import TYPE_CHECKING, Any

from aiogram.utils.callback_answer import CallbackAnswerMiddleware

if TYPE_CHECKING:
    from aiogram import Dispatcher
    from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker


def register_middlewares(
    dp: Dispatcher,
    dependencies: dict[str, Any],
    sessionmaker: async_sessionmaker[AsyncSession],
) -> None:
    from .database import DatabaseMiddleware
    from .dependency import DependencyMiddleware
    from .logger import LoggingMiddleware
    from .throttling import ThrottlingMiddleware

    dp.message.outer_middleware(ThrottlingMiddleware())

    dp.update.outer_middleware(LoggingMiddleware())

    dp.update.outer_middleware(DependencyMiddleware(dependencies))

    dp.update.outer_middleware(DatabaseMiddleware(sessionmaker))

    dp.callback_query.middleware(CallbackAnswerMiddleware())

