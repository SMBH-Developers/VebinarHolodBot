from aiogram import types
from aiogram.dispatcher.filters import Text
import asyncio
from aiogram.dispatcher.storage import FSMContext

from loader import dp
from texts import menu_registration, menu_about_web, menu_about_anastasia, menu_present, main_menu
from kbs import register_button
from src.constants import DATA_DIR
from src.models.db_sendings import mark_got_autosending_1, mark_got_autosending_2
from src.models.db import check_user
from src.states import States


@dp.message_handler(Text("Регистрация"))
async def registration_handler(message: types.Message):
    await message.answer(menu_registration, reply_markup=register_button)
    await mark_got_autosending_2(message.from_user.id)


@dp.message_handler(Text("Узнать о вебинаре"))
async def about_web_handler(message: types.Message, state: FSMContext):
    await message.answer_video_note(video_note="DQACAgIAAxkBAAIBcmV4h6ugOscGJUgzLwZlz5r5RGCKAAKQOQACUsTAS9_e73rLK0n6MwQ")
    
    await message.answer(menu_about_web(), reply_markup=register_button)
    await mark_got_autosending_1(message.from_user.id)


@dp.message_handler(Text("Об Анастасии"))
async def about_anastasia_handler(message: types.Message, state: FSMContext):
    photo_id = await message.answer_photo(types.InputFile(DATA_DIR / "media" / "anastasia.jpeg"))
    await message.answer(menu_about_anastasia)


@dp.message_handler(Text("Подарок"))
async def present_handler(message: types.Message):
    await message.answer(menu_present)
    await message.answer_document(types.InputFile(DATA_DIR / "media" / "ресурсные действия 01.pdf"))


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