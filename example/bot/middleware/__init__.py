from __future__ import annotations

from typing import TYPE_CHECKING, Any

from aiogram.utils.callback_answer import CallbackAnswerMiddleware
from aiogram_i18n import I18nMiddleware
from aiogram_i18n.cores import FluentCompileCore

if TYPE_CHECKING:
    from aiogram import Dispatcher
    from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker


def register_middlewares(
    dp: Dispatcher,
    dependencies: dict[str, Any],
    sessionmaker: async_sessionmaker[AsyncSession],
    default_locale: str,
) -> None:
    from .analytics import AnalyticsMiddleware
    from .database import DatabaseMiddleware
    from .dependency import DependencyMiddleware
    from .i18n import UserManager
    from .logger import LoggingMiddleware
    from .throttling import ThrottlingMiddleware
    from .user_register import UserRegisterMiddleware

    dp.message.outer_middleware(ThrottlingMiddleware())

    dp.update.outer_middleware(AnalyticsMiddleware())

    dp.update.outer_middleware(LoggingMiddleware())

    dp.update.outer_middleware(DependencyMiddleware(dependencies))

    dp.update.outer_middleware(DatabaseMiddleware(sessionmaker))

    dp.message.middleware(UserRegisterMiddleware())

    dp.callback_query.middleware(CallbackAnswerMiddleware())

    i18n_middleware = I18nMiddleware(
        core=FluentCompileCore(
            path="locales/{locale}/LC_MESSAGES",
        ),
        manager=UserManager(),
        default_locale=default_locale,
    )
    i18n_middleware.setup(dispatcher=dp)

