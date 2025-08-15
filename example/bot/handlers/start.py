from __future__ import annotations

from typing import TYPE_CHECKING

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram_dialog import StartMode

from bot.states import ExampleSG

if TYPE_CHECKING:
    from aiogram import types
    from aiogram_dialog import DialogManager
    from aiogram_i18n import I18nContext

router = Router()


@router.message(CommandStart())
async def handle_start_command(
    message: types.Message,
    dialog_manager: DialogManager,
    i18n: I18nContext,
) -> None:
    await message.answer("👋")

    await message.answer(i18n.get("start"))

    await dialog_manager.start(
        ExampleSG.example,
        mode=StartMode.RESET_STACK,
    )

