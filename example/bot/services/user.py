from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import exists, select, update

from bot.cache.redis import build_key, cached, clear_cache
from bot.database.models import UserModel
from bot.services import errors

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


@cached(key_builder=lambda session, user_id: build_key(user_id))
async def user_exists(
    session: AsyncSession,
    user_id: int,
) -> bool:
    """Check if a user exists."""
    query = select(exists().where(UserModel.id == user_id))
    result = await session.scalar(query)
    return bool(result)


@cached(key_builder=lambda session, user_id: build_key(user_id))
async def get_user(
    session: AsyncSession,
    user_id: int,
) -> UserModel | None:
    """Get a user by their Telegram ID."""
    return await session.get(UserModel, user_id)


async def create_user(
    session: AsyncSession,
    user_id: int,
    username: str | None,
    first_name: str | None,
    last_name: str | None,
    deep_link: str | None,
) -> UserModel:
    """Create a new user."""
    new_user = UserModel(
        id=user_id,
        username=username,
        first_name=first_name,
        last_name=last_name,
        deep_link=deep_link,
    )

    session.add(new_user)
    await session.flush()
    await clear_cache(user_exists, user_id)
    await clear_cache(get_user, user_id)

    return new_user


async def set_has_blocked_bot(
    session: AsyncSession,
    user_id: int,
    *,
    has_blocked_bot: bool,
) -> None:
    """Set has_blocked_bot flag for a user.

    Raises:
        UserNotFoundError: If user not found.

    """
    user = await get_user(session, user_id)

    if user is None:
        msg = f"user {user_id} not found"
        raise errors.UserNotFoundError(msg)

    if user.has_blocked_bot == has_blocked_bot:
        return

    await session.execute(update(UserModel).where(UserModel.id == user_id).values(has_blocked_bot=has_blocked_bot))

    await clear_cache(get_user, user_id)
