from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine

if TYPE_CHECKING:
    from sqlalchemy import URL


def _get_engine(url: URL | str) -> AsyncEngine:
    return create_async_engine(
        url=url,
        pool_size=0,
    )


def get_sessionmaker(url: URL | str) -> async_sessionmaker[AsyncSession]:
    return async_sessionmaker(bind=_get_engine(url), autoflush=False, expire_on_commit=False)
