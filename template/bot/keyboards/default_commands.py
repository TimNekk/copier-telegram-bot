from __future__ import annotations

from typing import TYPE_CHECKING

from aiogram.types import BotCommand, BotCommandScopeDefault

if TYPE_CHECKING:
    from aiogram import Bot

user_commands = [
    BotCommand(command="start", description="🚀 Start bot"),
]


async def set_default_commands(bot: Bot) -> None:
    await remove_default_commands(bot)

    await bot.set_my_commands(
        commands=user_commands,
        scope=BotCommandScopeDefault(),
    )


async def remove_default_commands(bot: Bot) -> None:
    await bot.delete_my_commands(scope=BotCommandScopeDefault())
