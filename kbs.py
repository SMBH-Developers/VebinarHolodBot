from aiogram import types

__all__ = ["main_board", "registration_board", "back_button"]


main_board = types.InlineKeyboardMarkup()
main_board.add(*[
    types.InlineKeyboardButton("Регистрация", callback_data="register"),
    types.InlineKeyboardButton("Узнать о вебинаре", callback_data="AboutWeb")
])
main_board.row(*[
    types.InlineKeyboardButton("Об Анастасии", callback_data="Anastasia"),
    types.InlineKeyboardButton("Подарок", callback_data="Present")
])


registration_board = types.InlineKeyboardMarkup(2)
registration_board.add(*[
    types.InlineKeyboardButton("Регистрация", url="https://soul-aca.ru/7steps", callback_data="register"),
    types.InlineKeyboardButton("Назад", callback_data="back")
])


back_button = types.InlineKeyboardMarkup(1)
back_button.add(types.InlineKeyboardButton("Назад", callback_data="back"))


register_button = types.InlineKeyboardMarkup(1)
register_button.add(types.InlineKeyboardButton("Регистрация", url="https://soul-aca.ru/7steps"))

