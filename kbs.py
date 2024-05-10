from aiogram import types

from src.constants import URL

__all__ = ["main_board", "register_button_url", "register_button_callback"]


main_board = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=3)
main_board.row("Регистрация🌸")
main_board.row("Узнать о вебинаре😌")
main_board.row(*["Об Анастасии⭐️", "Подарок🙌"])

register_button_url = types.InlineKeyboardMarkup(1)
register_button_url.add(types.InlineKeyboardButton("Регистрация", url=URL))

register_button_callback = types.InlineKeyboardMarkup(1)
register_button_callback.add(types.InlineKeyboardButton("Регистрация", callback_data="register"))

admin_button_main = types.InlineKeyboardMarkup(1)
admin_button_main.add(types.InlineKeyboardButton("Сделать рассылку 🚀", callback_data="newsletter"))

admin_choice = types.InlineKeyboardMarkup(2)
admin_choice.add(types.InlineKeyboardButton("Да ✅", callback_data="admin?apply"))
admin_choice.add(types.InlineKeyboardButton("Нет ❌", callback_data="admin?cancel"))


cancel = types.InlineKeyboardMarkup()
cancel.add(types.InlineKeyboardButton("Отмена ❌", callback_data="admin?cancel"))

