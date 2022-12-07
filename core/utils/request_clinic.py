import requests
import json
from core.utils.classDoctors import Doctor


def get_requests_clinic(lpu_code='2801014', deport='49'):
    lpu = None
    resault = []
    heraders = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'user-agent': 'Mozilla / 5.0(X11;Ubuntu;Linuxx86_64;rv: 106.0)Gecko/20100101Firefox / 106.0'
    }
    url = f'https://uslugi.mosreg.ru/zdrav/doctor_appointment/api/doctors?lpuCode={lpu_code}&departmentId={deport}&doctorId=&days=14'
    data = requests.get(url=url, headers=heraders)
    json_data = json.loads(data.text)
    items = json_data.get('items')

    # находим по коду, поликлинику в Мытищах
    for i in items:
        if i.get('lpu_code') == lpu_code:
            lpu = i
            break
    # берем всех врачей из поликлиники пишем их именна и количество билетов test

    doctors = lpu.get('doctors')

    for doctor in doctors:
        displayName = doctor.get('displayName')
        if 'Кабинет' in displayName:
            continue

        weeks = {}

        week1 = doctor.get('week1')
        for day in week1:
            date = day.get('date')
            count_tickets_date = day.get('count_tickets')
            weeks[date] = count_tickets_date

        week2 = doctor.get('week2')
        for day in week2:
            date = day.get('date')
            count_tickets_date = day.get('count_tickets')
            weeks[date] = count_tickets_date
        resault.append(
            Doctor(doctor.get('displayName'), doctor.get('family'), doctor.get('room'), doctor.get('count_tickets'),
                   weeks))
        # resault.append({
        #     'name': doctor.get('displayName'),
        #     'family': doctor.get('family'),
        #     'room': doctor.get('room'),
        #     'count_tickets': doctor.get('count_tickets'),
        #     'week': weeks,
        #
        # })
    return resault


if __name__ == '__main__':
    get_requests_clinic()
