from aiogram import types
import asyncio
from datetime import datetime


from loader import bot
from src.constants import DATA_DIR
from src.models import User
from src.models.db import update_sended
from src.models.db_sendings import update_autosending_1, update_autosending_2
from texts import hour_after_registration
from kbs import register_button


async def send_present_after_about(user: int):  # TODO times
    await bot.send_document(user, types.InputFile(DATA_DIR / "media" / "ресурсные действия 01.pdf"))
    await update_autosending_1(user)


async def send_present_after_registration(user: User):
    if ((int(user.got_autosending_2.timestamp()) + (1 * 60)) - int(date.now().timestamp())) <= 0:
        await bot.send_document(user.id, types.InputFile(DATA_DIR / "media" / "ресурсные действия 01.pdf"))
        await update_autosending_2(user.id)


async def after_registration(user: User):#TODO USER
    
    if (int(user.registration_date.timestamp() + (1 * 60)) - int(date.now().timestamp()) <= 0) and not (user.newsletter_sended): #HOURS
        await bot.send_photo(user.id, types.InputFile(DATA_DIR / "media" / "Frame 1.png"), caption=hour_after_registration, reply_markup=register_button)
        await update_sended(user.id)
        return
    



# asyncio.run(after_registration())
    
