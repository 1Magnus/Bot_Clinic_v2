from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from core.utils.statesform import StepsForm
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from core.handlers.apsched import send_message_if_tickets_available, send_message_if_free_day
from datetime import datetime, timedelta
from aiogram import Bot
from core.utils.request_clinic import get_requests_clinic
from core.keyboards.reply import get_reply_keyboard_in_list
from core.keyboards.reply import get_reply_keyboard


async def get_list_doctors_lor(message: Message, state: FSMContext):
    await message.answer('Минутку, посмотрим что я смогу для Вас найти..')
    doctors = get_requests_clinic(lpu_code='2801011', deport='45')
    list_family_doctors = [doctor.family for doctor in doctors]
    for doctor in doctors:
        await message.answer(
            f"{doctor.name},\r\n"
            f"Tалонов - {doctor.count_tickets} \r\n"
            f"Ближайшая дата {doctor.get_first_dae_tickets()}",
            reply_markup=get_reply_keyboard_in_list(list_family_doctors))
    await state.update_data(doctors=doctors, lpu_code='2801011', deport='45')
    await state.set_state(StepsForm.GET_NAME_DOCTOR)


async def get_list_doctors_pediator(message: Message, state: FSMContext):
    await message.answer('Минутку, посмотрим что я смогу для Вас найти..')
    doctors = get_requests_clinic()
    list_family_doctors = [doctor.family for doctor in doctors]
    for doctor in doctors:
        await message.answer(
            f"{doctor.name},\r\n"
            f"Tалонов - {doctor.count_tickets} \r\n"
            f"Ближайшая дата {doctor.get_first_dae_tickets()}",
            reply_markup=get_reply_keyboard_in_list(list_family_doctors))
    await state.update_data(doctors=doctors, lpu_code='2801014', deport='49')
    await state.set_state(StepsForm.GET_NAME_DOCTOR)


async def get_name_doctors(message: Message, state: FSMContext):
    doctor = message.text

    context_data = await state.get_data()
    doctors = context_data.get('doctors')
    nedd_doctor = None
    for i in doctors:
        if i.family == doctor:
            await state.update_data(nedd_doctor=i)
            nedd_doctor = i
            break

    if nedd_doctor:
        await message.answer(f"Доктор - {nedd_doctor.family} - талонов {nedd_doctor.count_tickets} \r\n"
                             f"Ближайщая дата - {nedd_doctor.get_first_dae_tickets()} \r\n"
                             f"Ищем для него?", reply_markup=get_reply_keyboard())
        await state.set_state(StepsForm.ZERO_TICKET) if nedd_doctor.count_tickets == 0 else await state.set_state(
            StepsForm.GET_FREE_DAY)

    if nedd_doctor is None:
        await message.answer('Что то я не понял про какого доктора идет речь')


async def zero_tickets(message: Message, bot: Bot, state: FSMContext, apscheduler: AsyncIOScheduler):
    if message.text == "Да":
        await state.clear()
        context_data = await state.get_data()
        lpu_code = context_data['lpu_code']
        deport = context_data['deport']
        apscheduler.add_job(send_message_if_tickets_available, trigger='interval', minutes=60,
                            kwargs={'bot': bot, 'chat_id': message.from_user.id,
                                    'need_doctor': context_data['nedd_doctor'], 'lpu_code': lpu_code, 'deport': deport})
    await state.clear()


async def get_free_day(message: Message, bot: Bot, state: FSMContext, apscheduler: AsyncIOScheduler):
    if message.text == 'Да':
        context_data = await state.get_data()
        nedd_doctor = context_data['nedd_doctor']
        free_day = nedd_doctor.first_day_tickets
        lpu_code = context_data['lpu_code']
        deport = context_data['deport']
        apscheduler.add_job(send_message_if_free_day, trigger='interval', seconds=120,
                            kwargs={'bot': bot, 'chat_id': message.from_user.id,
                                    'doctor': nedd_doctor, 'free_day': free_day, 'lpu_code': lpu_code,
                                    'deport': deport})

    await state.clear()


async def cancel_search(message: Message, bot: Bot, state: FSMContext, apscheduler: AsyncIOScheduler):
    await state.clear()
    apscheduler.remove_all_jobs()
    await message.answer('Поиск билетов отменен!')
