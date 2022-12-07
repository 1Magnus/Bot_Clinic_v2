from aiogram import Bot, Dispatcher
from aiogram.types import Message, ContentType
from core.settings import settings
from core.handlers.basic import get_start, get_hello, get_inline
from core.filters.iscontact import IsTrueConnact
from core.handlers.contact import get_true_contact, get_fake_contact
from aiogram.filters import Command
from aiogram import F
import asyncio
import logging
from core.utils.commands import set_commands
from core.handlers.callback import select_macbook
from core.utils.callback import MacInfo
from core.middlewares.countermiddleware import CounterMiddleware
from core.middlewares.officehours import OfficeHorsMiddlewakre
from core.handlers import form
from core.utils.statesform import StepsForm
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from core.handlers import apsched
from datetime import datetime, timedelta
from core.middlewares.apshedmiddlewares import SchedulerMiddleware


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, text='Бот Марс-два запущен!')


async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Бот Марс-два выключен!')


async def start():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - %(name)s - "
                               "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
                        )
    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')

    dp = Dispatcher()
    scheduler = AsyncIOScheduler(timezone='Europe/Moscow')

    # scheduler.add_job(apsched.send_message_time, trigger='date', run_date=datetime.now() + timedelta(seconds=10),
    #                   kwargs={'bot': bot})
    # scheduler.add_job(apsched.send_message_cron, trigger='cron', hour=datetime.now().hour,
    #                   minute=datetime.now().minute + 1, start_date=datetime.now(),
    #                   kwargs={'bot': bot})
    #
    # scheduler.add_job(apsched.send_message_interval, trigger='interval', seconds=60, kwargs={'bot': bot})

    dp.update.middleware.register(SchedulerMiddleware(scheduler))

    # dp.message.middleware.register(CounterMiddleware())
    # dp.message.middleware.register(OfficeHorsMiddlewakre())
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    dp.message.register(form.get_list_doctors_lor, Command(commands="lor"))
    dp.message.register(form.get_list_doctors_pediator, Command(commands="pediator"))
    dp.message.register(form.get_name_doctors, StepsForm.GET_NAME_DOCTOR)
    dp.message.register(form.zero_tickets, StepsForm.ZERO_TICKET)
    dp.message.register(form.get_free_day, StepsForm.GET_FREE_DAY)
    dp.message.register(form.cancel_search, Command(commands=['cancel']))
    scheduler.start()

    # dp.callback_query.register(select_macbook, MacInfo.filter())

    # dp.message.register(get_location, F.location)

    dp.message.register(get_start, Command(commands=['start', 'run']))
    dp.message.register(get_hello, F.text == 'привет')

    # dp.message.register(get_photo, F.photo)

    # dp.message.register(get_true_contact, F.contact, IsTrueConnact())
    # dp.message.register(get_fake_contact, F.contact)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())
