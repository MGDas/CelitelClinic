import asyncio
import requests
from organization.models import Department, Organization

def connect():

    response = requests.get('https://test.studiovector.art/json/GetDepartments.json')
    return response.json()

async def save_in_db(code, codeparent, name, organ_code):

    try:
        organ_id = Organization.objects.only('id').get(code=organ_code)
    except Organization.DoesNotExist:
        organ_id = None

    organ, status = Department.objects.update_or_create(
        code=code,
        defaults={
            'codeparent': codeparent if codeparent else '-----',
            'name': name if name else '-----',
            'organization': organ_id
        }
    )
    if status:
        print(f"{organ}...................СОЗДАНО!")
    else:
        print(f"{organ}...................ОБНОВЛЕНО!")

async def main():

    data = connect()
    tasks = []

    for d in data:
        task = asyncio.create_task(save_in_db(d['code'], d['codeparent'], d['name'], d['organization_id']))
        tasks.append(task)

    await asyncio.gather(*tasks)
