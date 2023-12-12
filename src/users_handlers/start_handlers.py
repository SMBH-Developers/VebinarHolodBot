from aiogram import types
from aiogram.dispatcher.storage import FSMContext


from loader import dp
from kbs import main_board
from texts import start_message, main_menu
from src.models.db import registrate_if_not_exists, check_user
from src.states import States


@dp.message_handler(commands="start")
async def start_handler(message: types.Message):
    user_exists = await check_user(message.from_user.id)

    if not user_exists:
        await States.get_name.set()
        await message.answer(start_message)
        return

    await message.answer(main_menu, reply_markup=main_board)


@dp.message_handler(state=States.get_name)
async def register_user_handler(message: types.Message, state: FSMContext):
    await registrate_if_not_exists(message.from_id, message.text)
    text = "Спасибо большое!\n" + main_menu
    await message.answer(text, reply_markup=main_board)
    await state.finish()
