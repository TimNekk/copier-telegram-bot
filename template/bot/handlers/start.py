from __future__ import annotations

from typing import TYPE_CHECKING

from aiogram import Router
from aiogram.filters import CommandStart

if TYPE_CHECKING:
    from aiogram import types

router = Router()


@router.message(CommandStart())
async def process_start_command(
    message: types.Message,
) -> None:
    await message.answer("👋")
