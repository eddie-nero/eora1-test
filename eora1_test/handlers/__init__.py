from aiogram import Dispatcher

from eora1_test.handlers.common import register_handlers_common
from eora1_test.handlers.start import register_handlers_kitty_bread


def register_handlers(dp: Dispatcher):
    register_handlers_common(dp)
    register_handlers_kitty_bread(dp)
