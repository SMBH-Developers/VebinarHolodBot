from aiogram import types

__all__ = ["main_board", "registration_board", "back_button"]


main_board = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=3)
main_board.row("Регистрация🌸")
main_board.row("Узнать о вебинаре😌")
main_board.row(*["Об Анастасии⭐️", "Подарок🙌"])

register_button = types.InlineKeyboardMarkup(1)
register_button.add(types.InlineKeyboardButton("Регистрация", url="https://soul-aca.ru/7steps"))

