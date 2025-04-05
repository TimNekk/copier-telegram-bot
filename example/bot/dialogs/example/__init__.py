from __future__ import annotations

from aiogram import Router


def get_dialogs_router() -> Router:
    from .dialogs import example_dialog

    router = Router()
    router.include_router(example_dialog)

    return router
