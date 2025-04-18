from __future__ import annotations

import asyncio
import sys

from aiogram_dialog import setup_dialogs
from loguru import logger

from bot.core.loader import bot, dp, sessionmaker, settings
from bot.dialogs import get_dialogs_router
from bot.handlers import get_handlers_router
from bot.keyboards.default_commands import (
    remove_default_commands,
    set_default_commands,
)
from bot.middleware import register_middlewares


async def on_startup() -> None:
    logger.info("Bot starting...")

    register_middlewares(
        dp,
        dependencies={
            "settings": settings,
        },
        sessionmaker=sessionmaker,
    )

    dp.include_router(get_handlers_router())

    dp.include_router(get_dialogs_router())
    setup_dialogs(dp)

    await set_default_commands(bot)

    bot_info = await bot.get_me()
    logger.info(f"Name     - {bot_info.full_name}")
    logger.info(f"Username - @{bot_info.username}")
    logger.info(f"ID       - {bot_info.id}")

    logger.info("Bot started!")


async def on_shutdown() -> None:
    logger.info("Bot stopping...")

    await remove_default_commands(bot)

    await dp.storage.close()
    await dp.fsm.storage.close()

    await bot.delete_webhook()
    await bot.session.close()

    logger.info("Bot stopped!")


async def main() -> None:
    logger.add(
        sink=f"{settings.file_log.directory}/{settings.file_log.name}",
        level=settings.file_log.level,
        format="{time} | {level} | {module}:{function}:{line} | {message}",
        rotation="10 MB",
        compression="zip",
    )

    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    await dp.start_polling(
        bot,
        allowed_updates=dp.resolve_used_update_types(),
    )


if __name__ == "__main__":
    if sys.platform == "win32":
        from winloop import install
    else:
        from uvloop import install

    install()
    asyncio.run(main())
