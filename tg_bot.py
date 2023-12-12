import asyncio
import random
import re

import texts
import kbs

from aiogram import Bot, Dispatcher
from aiogram import executor, types, exceptions
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from aiogram.dispatcher.filters.state import StatesGroup, State

from datetime import datetime, timedelta
from loguru import logger

from src.common import settings
from src.models import db, db_sendings


class States(StatesGroup):
    get_user_date_for_horoscope_year = State()
    back_state = State()


storage = RedisStorage2(db=settings.redis_db, pool_size=40)
bot = Bot(settings.tg_token)
dp = Dispatcher(bot, storage=storage)


async def autosending_1():
    while True:
        ...
        await asyncio.sleep(5)


async def autosending_2():
    while True:
        ...
        await asyncio.sleep(5)


async def on_startup(_):
    asyncio.create_task(autosending_1())
    asyncio.create_task(autosending_2())


try:
    executor.start_polling(dp, on_startup=on_startup)
finally:
    stop = True
