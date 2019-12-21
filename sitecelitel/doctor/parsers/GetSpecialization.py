import asyncio
import requests
from doctor.models import Specialization

def connect(url):
    response = requests.get(url)
    return response.json()

async def save_in_db(code, name):

    special, status = Specialization.objects.update_or_create(
        code=code,
        name=name
    )

    if not status:
        print(f"{special}......ОБНОВЛЕНО!")
    else:
        print(f"{special}......СОЗДАНО!")

async def main():

    url = 'https://celitel05.ru/json/GetSpecialization.json'
    data = connect(url)

    tasks = []
    for d in data:
        task = asyncio.create_task(save_in_db(d['code'], d['name']))
        tasks.append(task)

    await asyncio.gather(*tasks)
