from __future__ import annotations

from .base import ServiceError


class UserServiceError(ServiceError):
    pass


class UserNotFoundError(UserServiceError):
    pass
