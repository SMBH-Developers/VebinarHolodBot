from aiogram import types

from src.constants import URL

__all__ = ["main_board", "registration_board", "back_button"]


main_board = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=3)
main_board.row("Регистрация🌸")
main_board.row("Узнать о вебинаре😌")
main_board.row(*["Об Анастасии⭐️", "Подарок🙌"])

register_button_url = types.InlineKeyboardMarkup(1)
register_button_url.add(types.InlineKeyboardButton("Регистрация", url=URL))

register_button_callback = types.InlineKeyboardMarkup(1)
register_button_callback.add(types.InlineKeyboardButton("Регистрация", callback_data="register"))