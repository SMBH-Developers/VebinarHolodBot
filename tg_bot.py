import asyncio
from datetime import datetime

from aiogram import executor

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from loguru import logger

from src.common import dp
from src import users_handlers, admin_handlers
from src.models import db
import src.gifts_newsletters as nwsl


async def scheduler_job():
    users = await db.get_users()

    for user in users:
        await nwsl.send_notification_before_webinar(user[0], user[1])


async def the_next_day_job():
    users = await db.the_next_day_users()
    logger.info(f"USERS TO NEXT_DAY {users}")
    for user in users:
        await nwsl.next_day_notif(user)


async def gifts():
    while True:
        users = await db.get_users_to_gift(10)
        for user in users:
            await nwsl.send_gift(user)

        await asyncio.sleep(5)


async def newsletter():
    while True:
        users = await db.get_users_to_newsletter(60)

        for user in users:
            await nwsl.send_after_registration(user)

        await asyncio.sleep(5)


async def on_startup(_):
    asyncio.create_task(nwsl.sending_text())
    asyncio.create_task(gifts())
    asyncio.create_task(newsletter())


scheduler = AsyncIOScheduler()
scheduler.add_job(scheduler_job, "cron", minute=00, hour=18)
scheduler.add_job(the_next_day_job, "cron", minute=00, hour=10)
scheduler.start()

logger.info("Бот начала работу!")
executor.start_polling(dp, on_startup=on_startup)
