from aiogram import Bot
from aiogram.types import CallbackQuery
from core.utils.callback import MacInfo


# async def select_macbook(call: CallbackQuery, bot: Bot):
#     model = call.data.split('_')[1]
#     size = call.data.split('_')[0]
#     answer = f'{call.message.from_user.first_name}, Ты выбрал ноутбук {model} - {size} '
#     await call.message.answer(answer)
#     await call.answer()

async def select_macbook(call: CallbackQuery, bot: Bot, callback_data: MacInfo):
    model = callback_data.model
    size = callback_data.size
    answer = f'{call.message.from_user.first_name}, Ты выбрал ноутбук {model} - {size} '
    await call.message.answer(answer)
    await call.answer()
