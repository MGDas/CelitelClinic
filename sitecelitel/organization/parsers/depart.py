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

    depart, status = Department.objects.update_or_create(
        code=code,
        defaults={
            'codeparent': codeparent if codeparent else '-----',
            'name': name if name else '-----'
        }
    )
    if organ_id:
        depart.organization_id = organ_id
        depart.save()

    if status:
        print(f"{depart}...................СОЗДАНО!")
    else:
        print(f"{depart}...................ОБНОВЛЕНО!")

async def main():

    data = connect()
    tasks = []

    for d in data:
        task = asyncio.create_task(save_in_db(d['code'], d['codeparent'], d['name'], d['organization_id']))
        tasks.append(task)

    await asyncio.gather(*tasks)
