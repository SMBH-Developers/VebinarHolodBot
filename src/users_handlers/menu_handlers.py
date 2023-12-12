from aiogram import types
from aiogram.dispatcher.filters import Text
import asyncio
from aiogram.dispatcher.storage import FSMContext

from src.common import dp
from texts import menu_registration, menu_about_web, menu_about_anastasia, menu_present, main_menu
from kbs import register_button
import src.constants as constants
import src.models.db as db



@dp.message_handler(Text("Регистрация"))
async def registration_handler(message: types.Message):
    await message.answer(menu_registration, reply_markup=register_button)
    await db.update_state(message.from_id, "waiting_gift")


@dp.message_handler(Text("Узнать о вебинаре"))
async def about_web_handler(message: types.Message):
    await message.answer_video_note(video_note=constants.VIDEO_NOTE_ID)
    
    await message.answer(menu_about_web(), reply_markup=register_button)
    await db.update_state(message.from_id, "waiting_gift")


@dp.message_handler(Text("Об Анастасии"))
async def about_anastasia_handler(message: types.Message):
    await message.answer_photo(photo=constants.ANASTASIA_ID)
    await message.answer(menu_about_anastasia)


@dp.message_handler(Text("Подарок"))
async def present_handler(message: types.Message):
    await message.answer(menu_present)
    await message.answer_document(document=constants.GIFT_ID)


# @dp.message_handler(content_types=types.ContentType.ANY)
# async def fgg(message):
#     print(message)


# @dp.callback_query_handler(Text("back"))
# async def back_handler(message: types.Message, state: FSMContext):
#     state_data = await state.get_data()
#     if state_data:
#         for message_id in state_data.values():
#             await messagebot.delete_message(call.message.chat.id, message_id)

#         await state.finish()

#     await call.message.delete()
#     await call.message.answer(main_menu, reply_markup=main_board)