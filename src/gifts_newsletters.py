from aiogram import types
import asyncio
from datetime import datetime


from src.common import bot
import src.constants as constants

import src.models.db as db

import aiogram.utils.exceptions as aiogram_ex

import texts
import kbs
from loguru import logger


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
    await bot.send_message(user_id, text=texts.an_hour_before_web(name), reply_markup=kbs.register_button_url)

# asyncio.run(after_registration())
    
