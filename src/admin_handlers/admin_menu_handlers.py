from aiogram import types
from aiogram.dispatcher.storage import FSMContext

import kbs
from src.common import dp, bot
import src.models.db as db
from src.states import AdminStates
from src.common import ADMIN_IDS
from sending_msg import send_msg


@dp.message_handler(lambda message: message.from_user.id in ADMIN_IDS, commands="admin", state="*")
async def admin_menu(message: types.Message):
    await bot.send_message(message.chat.id, text="Чтобы сделать рассылку нажмите на кноку ниже",
                           reply_markup=kbs.admin_button_main)


@dp.callback_query_handler(lambda call: call.from_user.id in ADMIN_IDS and call.data.startswith("admin?"), state="*")
async def sending_msg(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == "admin?cancel":
        await bot.send_message(callback.message.chat.id,
                               text="Чтобы сделать рассылку нажмите на кноку ниже",
                               reply_markup=kbs.admin_button_main)
        await state.finish()
    elif callback.data == "admin?apply":
        msg = await state.get_data(AdminStates.get_message)
        await send_msg(msg.get('get_message', ''))
        await callback.answer("Рассылка запущена")
        await state.finish()


@dp.callback_query_handler(lambda call: call.from_user.id in ADMIN_IDS and call.data == "newsletter", state="*")
async def set_message_newsletter(callback: types.CallbackQuery, state: FSMContext):
    await bot.send_message(callback.from_user.id,
                           text="Введите текст для рассылки, чтобы продолжить. Нажмите на кнопку ниже для отмены\n\n"
                                "(файлы, фото, видео не отправлять, а так же текст с разным шрифтом)",
                           reply_markup=kbs.cancel)
    await state.set_state(AdminStates.get_message)


@dp.message_handler(state=AdminStates.get_message, content_types=types.ContentType.TEXT)
async def get_message(message: types.Message, state: FSMContext):
    msg = message.text
    await state.update_data(get_message=msg)
    await bot.send_message(message.from_user.id,
                           text=f"Давайте проверим все ли правильно вы написали\n"
                                f"Вот ваш текст:\n\n{msg}",
                           reply_markup=kbs.admin_choice)
