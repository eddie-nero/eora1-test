from aiogram import Dispatcher
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from eora1_test.middlewares.messages import MsgSavingMiddleware


def setup_middlewares(dp: Dispatcher):
    dp.middleware.setup(LoggingMiddleware())
    dp.middleware.setup(MsgSavingMiddleware())
