from __future__ import annotations

from aiogram import Router


def get_handlers_router() -> Router:
    from . import error, start, user_block

    router = Router(name=__name__)
    router.include_router(error.router)
    router.include_router(user_block.router)
    router.include_router(start.router)

    return router
