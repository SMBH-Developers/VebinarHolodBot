import asyncio

import aiogram.utils.exceptions as aiogram_ex
from aiogram import types

import src.constants as constants
import src.models.db as db
from src.common import bot

import texts
import kbs
from loguru import logger


from datetime import datetime

def catch_errors(func):
    async def __wrap(*args, **kwargs):
        try:
            await func(*args, **kwargs)

        except aiogram_ex.BotBlocked:
            logger.error(f"User:{args[0]} block bot")
            
        return
    
    return __wrap



@catch_errors
async def send_gift(user_id: int):
    await bot.send_document(user_id, document=constants.GIFT_AFTER_REGISTER)
    await db.update_state(user_id, "main")
    await db.update_sent_sendings(user_id)


@catch_errors
async def send_after_registration(user_id: int):
    await bot.send_photo(user_id, photo=constants.AFTER_HOUR_ID, caption=texts.hour_after_registration, reply_markup=kbs.register_button_url)
    await db.update_sended(user_id)


@catch_errors
async def send_notification_before_webinar(user_id: id, name: str):
    get_counts = await db.get_before_web(user_id)
    if get_counts == 2:
        print(f"Пользователь {user_id} уже получил 2 уведомления")
        return
    try:
        await bot.send_message(user_id, text=texts.an_hour_before_web(name), reply_markup=kbs.register_button_url)
    
    except aiogram_ex.ChatNotFound as ex:
        logger.exception(f"Chat not found {user_id=}")
        return
    
    get_counts += 1
    await db.set_before_web(user_id, get_counts)
    logger.info(f"Newsletter hour before web USER={user_id}")
# asyncio.run(after_registration())


@catch_errors
async def next_day_notif(user_id: int):
    await bot.send_message(user_id, texts.the_next_day)
    print(f"Sended 'next day notification' to {user_id=}")
    
