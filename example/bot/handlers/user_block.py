from __future__ import annotations

from typing import TYPE_CHECKING

from aiogram import Router
from aiogram.filters import ChatMemberUpdatedFilter
from aiogram.filters.chat_member_updated import KICKED, MEMBER
from loguru import logger

from bot.services import errors
from bot.services import user as user_service

if TYPE_CHECKING:
    from aiogram import types
    from posthog import Posthog
    from sqlalchemy.ext.asyncio import AsyncSession

router = Router(name=__name__)


@router.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=KICKED))
async def handle_user_blocked_bot(
    event: types.ChatMemberUpdated,
    session: AsyncSession,
    posthog: Posthog,
) -> None:
    try:
        await user_service.set_has_blocked_bot(session, event.from_user.id, has_blocked_bot=True)
    except errors.UserNotFoundError:
        logger.error(f"user {event.from_user.id} not found")
    else:
        posthog.capture(
            event="bot_blocked",
            properties={
                "$set": {
                    "has_blocked_bot": True,
                },
            },
        )
        logger.info(f"user {event.from_user.id} blocked bot")


@router.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=MEMBER))
async def handle_user_unblocked_bot(
    event: types.ChatMemberUpdated,
    session: AsyncSession,
    posthog: Posthog,
) -> None:
    try:
        await user_service.set_has_blocked_bot(session, event.from_user.id, has_blocked_bot=False)
    except errors.UserNotFoundError:
        logger.error(f"user {event.from_user.id} not found")
    else:
        posthog.capture(
            event="bot_unblocked",
            properties={
                "$set": {
                    "has_blocked_bot": False,
                },
            },
        )
        logger.info(f"user {event.from_user.id} unblocked bot")
