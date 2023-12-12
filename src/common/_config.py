from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from ._settings import settings


__all__ = ["bot", "storage", "dp", "ADMIN_IDS"]


bot = Bot(settings.tg_token, parse_mode="html")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

ADMIN_IDS = (1188441997, 791363343, 585807159, 6018479151)
