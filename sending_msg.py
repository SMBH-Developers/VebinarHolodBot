import asyncio

from aiogram import executor
from aiogram.utils import markdown
from loguru import logger

from src.common import bot, dp
from src.models import db


async def send_msg(_):
    count = 0
    count_ex = 0
    logger.info("Рассылка сообщения по все БД началась")
    all_users = await db.get_all_users()

    for user in all_users:
        text = f'{markdown.hbold("Мы уже в эфире!")}\n\nТы с нами?\n\nЯ считаю, что эта встреча не случайна — люди приходят в нашу жизнь не просто так.\n\nЯ готова делиться с тобой всеми ценными знаниями и опытом, примешь ли ты их?\n\nЧтобы ничего не пропустить, переходи по ссылке прямо сейчас  👇\n\nСсылка 👉https://course.soul-aca.ru/7step_in'
        await asyncio.sleep(0.1)
        try:
            await bot.send_message(user[0], text)
            count += 1
        except Exception as e:
            count_ex += 1
            logger.error(f"Пользователь {user} не получил сообщение - {e}")
    logger.info(f"Рассылка сообщения Закончилась\n\nОтправлено - {count}\n\nОшибки - {count_ex}")

executor.start_polling(dp, on_startup=send_msg)
