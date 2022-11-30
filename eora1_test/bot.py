import logging

import nest_asyncio
from aiogram import Bot
from aiogram.types import BotCommand
from aiogram.utils.executor import set_webhook

from eora1_test import config
from eora1_test.api.routes import setup_routes
from eora1_test.handlers import register_handlers
from eora1_test.loader import bot, dp, app, db, loop
from eora1_test.middlewares import setup_middlewares


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Начать диалог"),
        BotCommand(command="/cancel", description="Отменить текущее действие"),
        BotCommand(command="/history", description="История ответов"),
    ]
    await bot.set_my_commands(commands)


async def on_startup(dispatcher):
    await bot.set_webhook(config.WEBHOOK_URL, drop_pending_updates=True)
    await set_commands(bot)
    await db.create_tables()


async def on_shutdown(dispatcher):
    logging.warning('Shutting down..')
    await bot.delete_webhook()
    logging.warning('Bye!')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    nest_asyncio.apply()
    setup_middlewares(dp)
    register_handlers(dp)
    setup_routes(app)

    executor = set_webhook(
        dispatcher=dp,
        webhook_path=config.WEBHOOK_PATH,
        skip_updates=True,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        web_app=app,
    )
    executor.run_app(
        host=config.WEBAPP_HOST,
        port=config.WEBAPP_PORT,
        loop=loop,
    )
