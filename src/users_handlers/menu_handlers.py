from aiogram import types
from aiogram.dispatcher.filters import Text
import asyncio
from aiogram.dispatcher.storage import FSMContext

from loader import dp
from texts import menu_registration, menu_about_web, menu_about_anastasia, menu_present, main_menu
from kbs import registration_board, main_board, back_button
from src.constants import DATA_DIR


@dp.callback_query_handler(Text("register"))
async def registration_handler(call: types.CallbackQuery):
    #TODO отправить подарок
    await call.message.edit_text(menu_registration, reply_markup=registration_board, parse_mode="Markdown")


@dp.callback_query_handler(Text("AboutWeb"))
async def about_web_handler(call: types.CallbackQuery, state: FSMContext):
    video_note_id = await call.bot.send_video_note(call.message.chat.id, video_note=open(DATA_DIR / "media" / "video.mp4", "rb"))
    await state.update_data({"video_note_id":video_note_id.message_id})

    await call.message.delete()
    await asyncio.sleep(1)
    await call.message.answer(menu_about_web(), reply_markup=registration_board, parse_mode="Markdown")


@dp.callback_query_handler(Text("Anastasia"))
async def about_anastasia_handler(call: types.CallbackQuery, state: FSMContext):
    
    await call.message.delete()
    photo_id = await call.message.answer_photo(types.InputFile(DATA_DIR / "media" / "anastasia.jpeg"))
    await state.update_data({"photo_id":photo_id.message_id})
    await call.message.answer(menu_about_anastasia, reply_markup=back_button, parse_mode="Markdown")


@dp.callback_query_handler(Text("Present"))
async def present_handler(call: types.CallbackQuery):
    await call.message.edit_text(menu_present, reply_markup=back_button, parse_mode="Markdown")
    await call.message.answer_document(types.InputFile(DATA_DIR / "media" / "ресурсные действия 01.pdf"))


@dp.callback_query_handler(Text("back"))
async def back_handler(call: types.CallbackQuery, state: FSMContext):
    state_data = await state.get_data()
    if state_data:
        for message_id in state_data.values():
            await call.bot.delete_message(call.message.chat.id, message_id)

        await state.finish()

    await call.message.delete()
    await call.message.answer(main_menu, reply_markup=main_board, parse_mode="Markdown")