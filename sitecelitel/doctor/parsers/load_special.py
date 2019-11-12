import asyncio
import json
import os
from doctor.models import Specialization

pwd = os.path.dirname(os.path.dirname(__file__))

async def reader():

    with open(f'{pwd}/files/GetSpecialization.json', 'r') as file:
        return json.load(file)

async def save_in_db(code, name):

    special, s = Specialization.objects.get_or_create(
        code=code,
        name=name,
    )
    special.save()
    print(f"{special}...................{s}")

async def main():

    data = await reader()
    tasks = []

    for d in data:
        task = asyncio.create_task(save_in_db(d['code'], d['name']))
        tasks.append(task)

    await asyncio.gather(*tasks)
