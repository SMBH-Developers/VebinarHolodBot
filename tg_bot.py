import asyncio
import random
import re

import texts
import kbs

from aiogram import executor, types, exceptions
from aiogram.dispatcher import FSMContext

from datetime import datetime, timedelta
from loguru import logger

from src.common import settings
from src.models import db, db_sendings
from loader import dp
import src.users_handlers








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

