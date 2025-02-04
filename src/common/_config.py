from aiogram import Bot, Dispatcher
#from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from ._settings import settings


__all__ = ["bot", "storage", "dp", "ADMIN_IDS"]


bot = Bot(settings.tg_token, parse_mode="html")
#storage = MemoryStorage()
storage = RedisStorage2(db=settings.redis_db, pool_size=30)
dp = Dispatcher(bot, storage=storage)

ADMIN_IDS = (1188441997, 791363343, 585807159, 6018479151, 923202245, 1371617744)
