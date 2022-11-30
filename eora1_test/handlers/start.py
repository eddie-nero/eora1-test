from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

yes_variants = {'да', 'конечно', 'ага', 'пожалуй'}
no_variants = {'нет', 'нет, конечно', 'ноуп', 'найн'}


class KittyOrBread(StatesGroup):
    waiting_for_shape = State()
    waiting_for_ears = State()


async def kitty_bread_start(message: types.Message, state: FSMContext):
    await message.answer('Привет! Я помогу отличить кота от хлеба! Объект перед тобой квадратный?')
    await state.set_state(KittyOrBread.waiting_for_shape.state)


async def shape_chosen(message: types.Message, state: FSMContext):
    user_message = message.text.lower()
    if user_message not in (yes_variants | no_variants):
        await message.answer("Пожалуйста, ответьте утвердительно или отрицательно.")
        return
    if user_message in no_variants:
        await message.answer("Это кот, а не хлеб! Не ешь его!")
        await state.finish()
        return
    await state.set_state(KittyOrBread.waiting_for_ears.state)
    await message.answer("У него есть уши?")


async def ears_chosen(message: types.Message, state: FSMContext):
    if message.text.lower() not in (yes_variants | no_variants):
        await message.answer("Пожалуйста, ответьте утвердительно или отрицательно.")
        return
    if message.text.lower() in yes_variants:
        await message.answer("Это кот, а не хлеб! Не ешь его!")
    if message.text.lower() in no_variants:
        await message.answer("Это хлеб, а не кот! Ешь его!")
    await state.finish()


def register_handlers_kitty_bread(dp: Dispatcher):
    dp.register_message_handler(kitty_bread_start, commands="start", state="*")
    dp.register_message_handler(shape_chosen, state=KittyOrBread.waiting_for_shape)
    dp.register_message_handler(ears_chosen, state=KittyOrBread.waiting_for_ears)
