import logging

from aiogram import Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher
from aiogram.types import BotCommand
from aiogram.utils.executor import set_webhook
from aiohttp import web

from eora1_test import config
from eora1_test.handlers.common import register_handlers_common
from eora1_test.handlers.start import register_handlers_kitty_bread

bot = Bot(token=config.BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
dp.middleware.setup(LoggingMiddleware())


async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Начать диалог"),
        BotCommand(command="/cancel", description="Отменить текущее действие"),
    ]
    await bot.set_my_commands(commands)


async def on_startup(dispatcher):
    await bot.set_webhook(config.WEBHOOK_URL, drop_pending_updates=True)
    await set_commands(bot)


async def on_shutdown(dispatcher):
    logging.warning('Shutting down..')
    await bot.delete_webhook()
    logging.warning('Bye!')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    
    register_handlers_common(dp)
    register_handlers_kitty_bread(dp)
    
    app = web.Application()
    app.add_routes([web.get('/', handle),
                    web.get('/{name}', handle)])
    
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
    )
