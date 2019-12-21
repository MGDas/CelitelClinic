import requests
import logging
import asyncio
from doctor.models import Specialization, Doctor
from service.models import Service, ServiceGroup

def connect(url):

    response = requests.get(url)
    return response.json()

async def get_doctors(doctors):

    # В дальнейшем этот код нужно заменить на проверку докторов с док-кодом
    doc_list = []
    if doctors:
        for doc in doctors:
            try:
                doctor = Doctor.objects.get(code=doc['doccode'])
            except Doctor.DoesNotExist:
                continue

            doc_list.append(doctor)
            print(f'..................Доктор....{doctor.code}')

    return doc_list

async def save_in_db(code, name, cg, time, doctors):

    # Проверка на наличие группы услуги
    try:
        group = ServiceGroup.objects.get(code=cg)
    except ServiceGroup.DoesNotExist as e:
        group = False

    doc_list = await get_doctors(doctors)

    if group:
        update_field = {
            'name' : name,
            'service_group' : group,
            'time' : int(time) if time else 0,
        }

        service, status = Service.objects.update_or_create(
            code=code,
            defaults=update_field
        )
        if doc_list:
            service.doctors.add(*doc_list)
        service.save()

        if not status:
            print(f"{service}......услуга ОБНОВЛЕНА!")
        else:
            print(f"{service}......услуга СОЗДАНА!")


async def main():

    url = 'https://celitel05.ru/json/GetServices.json'
    data = connect(url)
    tasks = []
    for d in data:
        task = asyncio.create_task(save_in_db(
                d['code'],
                d['name'],
                d['group_id'],
                d['time'],
                d['doctors']
            )
        )
        tasks.append(task)

    await asyncio.gather(*tasks)
