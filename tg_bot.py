import asyncio
import random
import re

import texts
import kbs

from aiogram import executor, types, exceptions
from aiogram.dispatcher import FSMContext

from datetime import datetime, timedelta
from loguru import logger

from src.newsletter import after_registration, send_present_after_about, send_present_after_registration
from src.common import settings
from src.models import db, db_sendings
from loader import dp
from src.models.db import users_for_today
from src.models.db_sendings import get_users_autosending_1, get_users_autosending_2
import src.users_handlers








async def autosending_1():
    while True:
        users = await get_users_autosending_1()
        if not users:
            await asyncio.sleep(5)
            continue

        for user in users:
            await send_present_after_about(user)

        await asyncio.sleep(5)


async def autosending_2():
    while True:
        users = await get_users_autosending_2()
        if not users:
            await asyncio.sleep(5)
            continue

        for user in users:
            await send_present_after_registration(user)
            
        await asyncio.sleep(5)


async def newsletter():
    while True:
        print("start")
        users = await users_for_today()
        if not users:
            await asyncio.sleep(5)
            continue

        for user in users:
            await after_registration(user)

        await asyncio.sleep(5)


async def on_startup(_):
    asyncio.create_task(autosending_1())
    asyncio.create_task(autosending_2())
    asyncio.create_task(newsletter())


try:
    executor.start_polling(dp, on_startup=on_startup)
finally:
    stop = True

