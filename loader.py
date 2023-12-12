from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from src.common import settings
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = RedisStorage2(db=settings.redis_db, pool_size=40)
bot = Bot(settings.tg_token)
dp = Dispatcher(bot, storage=MemoryStorage()) #TODO use redis