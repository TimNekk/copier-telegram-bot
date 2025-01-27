from __future__ import annotations

from functools import wraps
from typing import TYPE_CHECKING, Any

from bot.cache.serialization import AbstractSerializer, PickleSerializer
from bot.core.loader import redis_client

if TYPE_CHECKING:
    from collections.abc import Callable
    from datetime import timedelta

    from redis.asyncio import Redis

DEFAULT_TTL = 10


def build_key(*args: tuple[str, Any], **kwargs: dict[str, Any]) -> str:
    """Build a string key based on provided arguments and keyword arguments."""
    args_str = ":".join(map(str, args))
    kwargs_str = ":".join(f"{key}={value}" for key, value in sorted(kwargs.items()))
    return f"{args_str}:{kwargs_str}"


async def set_redis_value(
    key: bytes | str,
    value: bytes | str,
    ttl: int | timedelta | None = DEFAULT_TTL,
    is_transaction: bool = False,
) -> None:
    """Set a value in Redis with an optional time-to-live (TTL)."""
    async with redis_client.pipeline(transaction=is_transaction) as pipeline:
        await pipeline.set(key, value)
        if ttl:
            await pipeline.expire(key, ttl)

        await pipeline.execute()


def cached(
    ttl: int | timedelta = DEFAULT_TTL,
    namespace: str = "main",
    cache: Redis = redis_client,
    key_builder: Callable[..., str] = build_key,
    serializer: AbstractSerializer | None = None,
) -> Callable:
    """Cache the functions return value into a key generated with module_name, function_name and args."""
    if serializer is None:
        serializer = PickleSerializer()

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        async def wrapper(*args: tuple[str, Any], **kwargs: dict[str, Any]) -> Any:
            key = key_builder(*args, **kwargs)
            key = f"{namespace}:{func.__module__}:{func.__name__}:{key}"

            # Check if the key is in the cache
            cached_value = await cache.get(key)
            if cached_value is not None:
                return serializer.deserialize(cached_value)

            # If not in cache, call the original function
            result = await func(*args, **kwargs)

            # Store the result in Redis
            await set_redis_value(
                key=key,
                value=serializer.serialize(result),
                ttl=ttl,
            )

            return result

        return wrapper

    return decorator


async def clear_cache(
    func: Callable,
    *args: Any,
    **kwargs: Any,
) -> None:
    """Clear the cache for a specific function and arguments.

    :param func: Function to clear cache for.
    :param args: Arguments to pass to the function.
    :param kwargs: Keyword arguments to pass to the function.
    """
    namespace: str = kwargs.get("namespace", "main")

    key = build_key(*args, **kwargs)
    key = f"{namespace}:{func.__module__}:{func.__name__}:{key}"

    await redis_client.delete(key)