from aiogram import types


from src.states import States
from src.models.db import check_user

def check_user_wrap(func):
    async def _wraper(args):
        if not (await check_user()):
            ...