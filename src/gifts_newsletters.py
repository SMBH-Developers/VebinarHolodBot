from aiogram import types
import asyncio
from datetime import datetime


from src.common import bot
import src.constants as constants

import src.models.db as db

import texts
from kbs import register_button


    
async def send_gift(user_id: int):
    await bot.send_document(user_id, document=constants.GIFT_AFTER_REGISTER)
    await db.update_state(user_id, "main")
    await db.update_sent_sendings(user_id)

async def send_after_registration(user_id: int):
    await bot.send_photo(user_id, photo=constants.AFTER_HOUR_ID, caption=texts.hour_after_registration, reply_markup=register_button)
    await db.update_sended(user_id)

async def send_notification_before_webinar(user_id: id, name: str):
    await bot.send_message(user_id, text=texts.an_hour_before_web(name), reply_markup=register_button)

# asyncio.run(after_registration())
    
