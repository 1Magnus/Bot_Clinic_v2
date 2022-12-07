from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from core.utils.callback import MacInfo

select_macbook = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Macbook',
            callback_data='apple_air'
        )
    ],
    [
        InlineKeyboardButton(
            text='HP',
            callback_data='apple_hp'
        )
    ],
    [
        InlineKeyboardButton(
            text='Macbook V2',
            callback_data='apple_air_v2'
        )
    ],
    [
        InlineKeyboardButton(
            text='Link',
            url='https://vk.ru'
        )
    ]
])


def get_inline_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Да', callback_data='yes')
    keyboard_builder.button(text='Нет', callback_data='no')
    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup()
