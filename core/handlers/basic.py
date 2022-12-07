from aiogram import Bot
from aiogram.types import Message
import json
from core.keyboards.reply import reply_keybord, local_tel_poll_keyboard, get_reply_keyboard
from core.keyboards.inline import select_macbook, get_inline_keyboard


async def get_inline(message: Message, bot: Bot):
    await message.answer(f' Hello {message.from_user.first_name} Inline keyboard',
                         reply_markup=get_inline_keyboard())


async def get_start(message: Message, bot: Bot):
    await message.reply(f'Привет, я добрый бот и помогу Вам найти талоны к нужному врачу!')

#
# async def get_location(message: Message, bot: Bot):
#     await message.answer(f'GEO!!!--- {message.location.latitude}\n{message.location.longitude}')
#
#
# async def get_photo(message: Message, bot: Bot):
#     await message.answer(f'You send IMG')
#     file = await bot.get_file(message.photo[-1].file_id)  # узнаем айди файла, а затем его скачиваем
#     await bot.download_file(file.file_path, 'photo.jpg')


async def get_hello(message: Message, bot: Bot):
    await message.answer('Hello and you')
    # json_str = json.dumps(message.dict(), default=str)
    # print(json_str)
