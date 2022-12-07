from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder

reply_keybord = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Ryd 1 Button 1'
        ),
        KeyboardButton(
            text='Ryd 1 Button 2'
        ),
        KeyboardButton(
            text='Ryd 1 Button 3'
        )],
    [
        KeyboardButton(
            text='Ryd 2 Button 1'
        ), KeyboardButton(
        text='Ryd 2 Button 2'
    ), KeyboardButton(
        text='Ryd 2 Button 3'
    ),
    ],
    [
        KeyboardButton(
            text='Ryd 3 Button 1'
        ), KeyboardButton(
        text='Ryd 3 Button 2'
    )
    ]

], resize_keyboard=True, one_time_keyboard=True)

local_tel_poll_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Geo',
            request_location=True)
    ],
    [
        KeyboardButton(
            text='Contact',
            request_contact=True)
    ],
    [
        KeyboardButton(
            text='Victor',
            request_poll=KeyboardButtonPollType())
    ]
], resize_keyboard=True, one_time_keyboard=False,
    input_field_placeholder='Отправь локацию, телефон или создай викторину')


def get_reply_keyboard():
    keyboard_builder = ReplyKeyboardBuilder()
    keyboard_builder.button(text='Да')
    keyboard_builder.button(text='Нет')
    return keyboard_builder.as_markup(reply_keybord=True, one_time_keyboard=True, resize_keyboard=True,
                                      input_field_placeholder='Ищем у этого доктора')


def get_reply_keyboard_in_list(list_doctors: list):
    keyboard_builder = ReplyKeyboardBuilder()
    for i in list_doctors:
        keyboard_builder.button(text=f'{i}')
    keyboard_builder.adjust(3)
    return keyboard_builder.as_markup(reply_keybord=True, one_time_keyboard=True, resize_keyboard=True,
                                      input_field_placeholder='Выбери фамилию доктора')
