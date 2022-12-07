from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='lor',
            description='Ищем ЛОРА'
        ),
        BotCommand(
            command='pediator',
            description='Ищем ПЕДИАТОРА'
        ),
        BotCommand(
            command='cancel',
            description='Сбросить'
        ),
        # BotCommand(
        #     command='inline',
        #     description='Показать инлай клавиатуру'
        # ),
        # BotCommand(
        #     command='form',
        #     description='Начать опрос'
        # ),


    ]
    await bot.set_my_commands(commands, BotCommandScopeDefault())
