import asyncio
from pathlib import Path

import aiogram.utils.exceptions as aiogram_ex
from aiogram import types

from .constants import PHOTOS_DIR
import src.models.db as db
from src.common import bot

import texts
import kbs
from loguru import logger


from datetime import datetime

def catch_errors(func):
    async def __wrap(*args, **kwargs):
        try:
            await func(*args, **kwargs)

        except aiogram_ex.BotBlocked:
            logger.error(f"User:{args[0]} block bot")
            
        return
    
    return __wrap


@catch_errors
async def send_gift(user_id: int):
    try:
        await bot.send_document(user_id, document=types.InputFile(str(Path('data/media/kod_sots_uspeha.pdf'))))
        await db.update_state(user_id, "main")
        await db.update_sent_sendings(user_id)
        logger.info(f"User - {user_id} get gift")
    except Exception as e:
        logger.exception(f"Error to send gift message for {user_id} - {e}")


@catch_errors
async def send_after_registration(user_id: int):
    try:
        await bot.send_photo(user_id, photo=types.InputFile(str(Path('data/media/Frame_1.png'))), caption=texts.hour_after_registration, reply_markup=kbs.register_button_url)
        await db.update_sended(user_id)
        logger.info(f"User - {user_id} get message after registration")
    except Exception as e:
        logger.exception(f"Error: User - {user_id} NOT get message after registration")


@catch_errors
async def send_notification_before_webinar(user_id: id, name: str):
    get_counts = await db.get_before_web(user_id)
    if get_counts == 2:
        print(f"Пользователь {user_id} уже получил 2 уведомления")
        return
    try:
        await bot.send_message(user_id, text=texts.an_hour_before_web(name), reply_markup=kbs.register_button_url)
        logger.info(f"User {user_id} get message before webinar")
    except aiogram_ex.ChatNotFound as ex:
        logger.exception(f"Chat not found {user_id}")
        return
    except Exception as e:
        logger.exception(f"Error 'before webinar'{user_id} - {e}")
        return
    
    get_counts += 1
    await db.set_before_web(user_id, get_counts)
    logger.info(f"Newsletter hour before web USER={user_id}")
# asyncio.run(after_registration())


@catch_errors
async def next_day_notif(user_id: int):
    try:
        await bot.send_message(user_id, texts.the_next_day)
        print(f"Sended 'next day notification' to {user_id}")
    except Exception as e:
        logger.error(f"Not Sended 'next day notification' to {user_id} - {e}")
    

async def sending_text():
    text = "Привет! У тебя все в порядке?\n\nКажется, я не видела тебя на мастер-классе, хотя точно видела твою регистрацию ⭐\n\nВозможно, у тебя не получилось присутствовать по своим причинам. Сегодня у тебя есть возможность посмотреть вебинар в 19:00 по Москве\n\nОткрой свое сердце переменам! Не пропусти 🌟\n\nПозже пришлю напоминание❤"
    white_day = 19
    now_time = datetime.now()
    if now_time.day > white_day:
        print('turned off')
        return
    logger.info("Рассылка большого блока началась")
    while True:
        now_time = datetime.now()
        if now_time.day == white_day and now_time.hour >= 16:
            users = db.users_sending_text()
            for user in users:
                now_time = datetime.now()
                if now_time.day != white_day:
                    break
                count = db.count_ppl_who_got()
                if count > 1000:
                    print('broke cause count > 1000')
                    return
                try:
                    await asyncio.sleep(0.5)
                    logger.info(f"Sending count: {count}")
                    await bot.send_message(user, text)
                    db.set_sending_text(user)
                    logger.info(f"User - {user} получил сообщение рассылки")
                    await asyncio.sleep(4)
                except Exception as ex:
                    logger.info(f"User_ID {user} получил ошибку: {ex}")
                finally:
                    await asyncio.sleep(1)
            return
        await asyncio.sleep(60)
    logger.info("Рассылка большого блока закончилась")
