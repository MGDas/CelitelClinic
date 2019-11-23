import asyncio
import requests
from organization.models import Organization

def connect():

    response = requests.get('http://test.studiovector.art/json/GetOrganizations.json')
    return response.json()

async def save_in_db(code, name):

    organ, status = Organization.objects.update_or_create(
        code=code,
        defaults={'name':name}
    )
    if status:
        print(f"{organ}...................СОЗДАНО!")
    else:
        print(f"{organ}...................ОБНОВЛЕНО!")

async def main():

    data = connect()
    tasks = []

    for d in data:
        task = asyncio.create_task(save_in_db(d['code'], d['name']))
        tasks.append(task)

    await asyncio.gather(*tasks)
