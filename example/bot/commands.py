from __future__ import annotations

from typing import TYPE_CHECKING

from aiogram.types import BotCommand, BotCommandScopeDefault

if TYPE_CHECKING:
    from aiogram import Bot

default_commands = [
    BotCommand(command="start", description="🚀 Start bot"),
]


async def set_commands(bot: Bot) -> None:
    await bot.set_my_commands(
        commands=default_commands,
        scope=BotCommandScopeDefault(),
    )


async def remove_commands(bot: Bot) -> None:
    await bot.delete_my_commands(scope=BotCommandScopeDefault())
