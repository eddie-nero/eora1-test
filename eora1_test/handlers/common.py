from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from eora1_test.loader import db


async def cmd_cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Диалог закончен. Чтобы начать заново отправьте `/start`")


async def read_history(message: types.Message):
    result = await db.load_all_user_messages(message.from_id)
    msg = '\n'.join(result)
    await message.answer(msg)


def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(read_history, commands="history", state="*")
    dp.register_message_handler(cmd_cancel, commands="cancel", state="*")
    dp.register_message_handler(cmd_cancel, Text(equals="отмена", ignore_case=True), state="*")
