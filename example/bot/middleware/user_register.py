from __future__ import annotations

from typing import TYPE_CHECKING, Any, TypeVar

from aiogram import BaseMiddleware
from aiogram.types import Message
from loguru import logger

from bot.services import user as user_service

if TYPE_CHECKING:
    from collections.abc import Awaitable, Callable

    from posthog import Posthog
    from sqlalchemy.ext.asyncio import AsyncSession

T = TypeVar("T")


class UserRegisterMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: dict[str, Any],
    ) -> T | None:
        if not isinstance(event, Message):
            return await handler(event, data)

        session: AsyncSession = data["session"]
        message: Message = event
        tg_user = message.from_user

        if not tg_user:
            return await handler(event, data)

        if not await user_service.user_exists(session, tg_user.id):
            deep_link = message.text[7:] if message.text and message.text.startswith("/start ") else None
            user = await user_service.create_user(
                session,
                user_id=tg_user.id,
                username=tg_user.username,
                first_name=tg_user.first_name,
                last_name=tg_user.last_name,
                deep_link=deep_link,
            )

            posthog: Posthog = data["posthog"]
            posthog.capture(
                event="user_registered",
                properties={
                    "$set": {
                        "username": tg_user.username,
                        "first_name": tg_user.first_name,
                        "last_name": tg_user.last_name,
                        "has_blocked_bot": False,
                    },
                    "$set_once": {
                        "deep_link": deep_link,
                    },
                },
            )
            logger.info(f"user {user.id} added to database")

        return await handler(event, data)
