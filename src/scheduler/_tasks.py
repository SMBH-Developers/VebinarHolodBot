from src.models.db import get_users
from loader import bot
from texts import an_hour_before_web
from kbs import register_button


async def notification_about_web():
    users = await get_users()

    for user in users:
        await bot.send_message(user.id, an_hour_before_web(user.name), reply_markup=register_button)
