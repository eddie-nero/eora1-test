from asyncio import get_event_loop

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiohttp import web

from eora1_test import config
from eora1_test.db_api.db import Database

bot = Bot(token=config.BOT_TOKEN)
storage = RedisStorage2(
    password=config.REDIS_PASSWORD if config.REDIS_PASSWORD else None,
    host=config.REDIS_HOST,
    port=config.REDIS_PORT,
    db=config.REDIS_DB_FSM,
)
# storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
app = web.Application()
loop = get_event_loop()
db = Database(loop)
