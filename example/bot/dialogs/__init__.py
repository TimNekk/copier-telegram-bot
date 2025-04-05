from __future__ import annotations

from aiogram import Router


def get_dialogs_router() -> Router:
    from . import example

    router = Router()
    router.include_router(example.get_dialogs_router())

    return router
