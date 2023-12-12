from aiogram.dispatcher.filters.state import StatesGroup, State

class States(StatesGroup):
    add_user = State()
    get_user_date_for_horoscope_year = State()
    back_state = State()