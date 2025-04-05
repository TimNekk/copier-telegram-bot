from __future__ import annotations

from aiogram import Router


def get_handlers_router() -> Router:
    from . import start

    router = Router()
    router.include_router(start.router)

    return router
