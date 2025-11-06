from __future__ import annotations

import inspect
from functools import wraps
from typing import TYPE_CHECKING, Any

from bot.cache.serialization import AbstractSerializer, PickleSerializer
from bot.core.loader import redis_client

if TYPE_CHECKING:
    from collections.abc import Callable
    from datetime import timedelta

    from redis.asyncio import Redis

MINUTE = 60
HOUR = 60 * MINUTE
DAY = 24 * HOUR
DEFAULT_TTL = 5 * MINUTE


def build_key(*args: Any, **kwargs: Any) -> str:
    """Build a string key based on provided arguments and keyword arguments."""
    args_str = ":".join(map(str, args))
    kwargs_str = ":".join(f"{key}={value}" for key, value in sorted(kwargs.items()))
    return f"{args_str}:{kwargs_str}"


def build_key_with_defaults(
    *param_names: str,
) -> Callable[[Callable], Callable[..., str]]:
    """Create a key builder factory that uses inspect to fill in default parameter values."""

    def factory(func: Callable) -> Callable[..., str]:
        sig = inspect.signature(func)

        def key_builder(*args: Any, **kwargs: Any) -> str:
            # Bind arguments to the function signature to get defaults
            bound = sig.bind(*args, **kwargs)
            bound.apply_defaults()

            # Extract only the specified parameters
            values = [bound.arguments.get(name) for name in param_names]
            return build_key(*(value for value in values if value is not None))

        return key_builder

    return factory


async def set_redis_value(
    key: bytes | str,
    value: bytes | str,
    ttl: int | timedelta | None = DEFAULT_TTL,
    *,
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
    key_builder: Callable[..., str] | Callable[[Callable], Callable[..., str]] = build_key,
    serializer: AbstractSerializer | None = None,
) -> Callable:
    """Cache the functions return value into a key generated with module_name, function_name and args."""
    if serializer is None:
        serializer = PickleSerializer()

    def decorator(func: Callable) -> Callable:
        # If key_builder is a factory (returns a callable when called with func), use it
        # Otherwise, use key_builder directly
        try:
            # Try calling key_builder with func - if it returns a callable, it's a factory
            test_result = key_builder(func)
            actual_key_builder = test_result if callable(test_result) else key_builder
        except (TypeError, ValueError):
            # If calling with func fails, it's not a factory, use it directly
            actual_key_builder = key_builder

        @wraps(func)
        async def wrapper(*args: Any, **kwargs: Any) -> Any:
            key = actual_key_builder(*args, **kwargs)
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
    namespace: str = "main",
    **kwargs: Any,
) -> None:
    """Clear the cache for a specific function and arguments.

    If an argument or keyword argument is not provided, it will be treated as a wildcard,
    matching all cache entries regardless of that parameter's value.
    """
    # Build partial key from only the provided args/kwargs
    partial_key = build_key(*args, **kwargs)

    # Handle empty key case (just ":") - match all entries for this function
    if partial_key and partial_key != ":":
        pattern = f"{namespace}:{func.__module__}:{func.__name__}:{partial_key}*"
    else:
        pattern = f"{namespace}:{func.__module__}:{func.__name__}:*"

    # Find all keys matching the pattern
    matching_keys = [key async for key in redis_client.scan_iter(match=pattern)]

    # Delete all matching keys
    if matching_keys:
        await redis_client.delete(*matching_keys)
