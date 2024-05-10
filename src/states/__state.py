from aiogram.dispatcher.filters.state import StatesGroup, State


class States(StatesGroup):
    get_name = State()


class AdminStates(StatesGroup):
    get_message = State()
