from aiogram import Bot
from core.utils.classDoctors import Doctor
from datetime import datetime
from core.utils.request_clinic import get_requests_clinic


# async def send_message_time(bot: Bot):
#     await bot.send_message(1453450924, f"Это сообщение отправлено через несколько сукунд после стратара бота")
#
#
# async def send_message_cron(bot: Bot):
#     await bot.send_message(1453450924, f"Ежеденвно в указанное время")
#
#
# async def send_message_interval(bot: Bot):
#     await bot.send_message(1453450924, f"Через определенный интервал!!!!!")


async def send_message_if_tickets_available(bot: Bot, chat_id: int, doctor: Doctor, lpu_code: str, deport: str):
    await bot.send_message(chat_id, f"Ищу билеты")
    respons = get_requests_clinic(lpu_code=lpu_code, deport=deport)
    for i in respons:
        if doctor.family == i.family:
            if i.count_tickets > 0:
                await bot.send_message(chat_id, f"У доктора {i.family} появились билеты!")
                break



async def send_message_if_free_day(bot: Bot, chat_id: int, doctor: Doctor, free_day: str, lpu_code: str, deport: str):
    last_free_day = datetime.strptime(free_day, '%d.%m.%Y')
    respons = get_requests_clinic(lpu_code=lpu_code, deport=deport)
    for i in respons:
        if doctor.family == i.family:
            new_day = i.get_first_dae_tickets()
            new_day = datetime.strptime(new_day, '%d.%m.%Y')
            if new_day < last_free_day:
                await bot.send_message(chat_id, f"У {i.family} - появился билет на более ближнюю дату!")
            # else:
            #     await bot.send_message(chat_id, f"У {i.family} - ближайшая дата не изменилась")
            break

