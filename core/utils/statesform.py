from aiogram.fsm.state import StatesGroup, State


class StepsForm(StatesGroup):
    GET_NAME_DOCTOR = State()
    ZERO_TICKET = State()
    GET_FREE_DAY = State()
