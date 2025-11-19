from __future__ import annotations

from typing import TYPE_CHECKING, Any, TypeVar

from aiogram import BaseMiddleware
from posthog import identify_context, new_context

if TYPE_CHECKING:
    from collections.abc import Awaitable, Callable

    from aiogram.types import Update

T = TypeVar("T")


class AnalyticsMiddleware(BaseMiddleware):
    def _extract_user_id(self, event: Update) -> str | None:  # noqa: C901, PLR0911, PLR0912
        """Extract user_id from different update types."""
        if event.message:
            msg = event.message
            return str(msg.from_user.id if msg.from_user else msg.chat.id)
        if event.edited_message:
            edited_msg = event.edited_message
            return str(edited_msg.from_user.id if edited_msg.from_user else edited_msg.chat.id)
        if event.channel_post:
            return str(event.channel_post.chat.id)
        if event.edited_channel_post:
            return str(event.edited_channel_post.chat.id)
        if event.business_message:
            biz_msg = event.business_message
            return str(biz_msg.from_user.id if biz_msg.from_user else biz_msg.chat.id)
        if event.edited_business_message:
            edited_biz_msg = event.edited_business_message
            return str(edited_biz_msg.from_user.id if edited_biz_msg.from_user else edited_biz_msg.chat.id)
        if event.callback_query:
            return str(event.callback_query.from_user.id)
        if event.inline_query:
            return str(event.inline_query.from_user.id)
        if event.chosen_inline_result:
            return str(event.chosen_inline_result.from_user.id)
        if event.shipping_query:
            return str(event.shipping_query.from_user.id)
        if event.pre_checkout_query:
            return str(event.pre_checkout_query.from_user.id)
        if event.poll_answer:
            if event.poll_answer.user:
                return str(event.poll_answer.user.id)
            if event.poll_answer.voter_chat:
                return str(event.poll_answer.voter_chat.id)
        if event.my_chat_member:
            return str(event.my_chat_member.from_user.id)
        if event.chat_member:
            return str(event.chat_member.from_user.id)
        if event.chat_join_request:
            return str(event.chat_join_request.from_user.id)
        if event.message_reaction:
            if event.message_reaction.user:
                return str(event.message_reaction.user.id)
            if event.message_reaction.actor_chat:
                return str(event.message_reaction.actor_chat.id)
        if event.purchased_paid_media:
            return str(event.purchased_paid_media.from_user.id)
        if event.business_connection:
            return str(event.business_connection.user.id)
        if event.chat_boost:
            boost_source = event.chat_boost.boost.source
            if hasattr(boost_source, "user") and boost_source.user:
                return str(boost_source.user.id)
        if event.removed_chat_boost:
            removed_source = event.removed_chat_boost.source
            if hasattr(removed_source, "user") and removed_source.user:
                return str(removed_source.user.id)
        return None

    async def __call__(
        self,
        handler: Callable[[Update, dict[str, Any]], Awaitable[Any]],
        event: Update,
        data: dict[str, Any],
    ) -> T | None:
        user_id = self._extract_user_id(event)

        if user_id is None:
            return await handler(event, data)

        with new_context():
            identify_context(user_id)
            return await handler(event, data)
