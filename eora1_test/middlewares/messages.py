from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware

from eora1_test.loader import db


class MsgSavingMiddleware(BaseMiddleware):
    
    def __init__(self):
        super(MsgSavingMiddleware, self).__init__()
    
    async def on_process_message(self, message: types.Message, data: dict):
        if not message.text.lower().startswith('/'):
            await db.save_message(message.from_id, message.text.lower())
