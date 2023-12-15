import asyncio
import random
import re

import texts
import kbs

from aiogram import executor, types, exceptions
from aiogram.dispatcher import FSMContext
from apscheduler.schedulers.asyncio import AsyncIOScheduler
# from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from datetime import datetime, timedelta
from loguru import logger


from src.common import dp
from src.models import db
import src.gifts_newsletters as nwsl
import src.users_handlers





async def scheduler_job():
    users = await db.get_users()

    for user in users:
        await nwsl.send_notification_before_webinar(user[0], user[1])

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
    asyncio.create_task(gifts())
    asyncio.create_task(newsletter())

scheduler = AsyncIOScheduler()
# scheduler.add_jobstore()
scheduler.add_job(scheduler_job, "cron", minute=0, hour=18)
scheduler.start()

try:
    executor.start_polling(dp, on_startup=on_startup)
finally:
    stop = True

