import asyncio
import requests
from organization.models import Organization

def connect():

    response = requests.get('https://celitel05.ru/json/GetOrganizations.json')
    return response.json()

async def save_in_db(code, name):

    organ, status = Organization.objects.update_or_create(
        code=code,
        defaults={'namefull':name}
    )
    if status:
        print(f"{organ}...................СОЗДАНО!")
    else:
        print(f"{organ}...................ОБНОВЛЕНО!")

async def main():

    data = connect()
    tasks = []

    for d in data:
        task = asyncio.create_task(save_in_db(d['code'], d['namefull']))
        tasks.append(task)

    await asyncio.gather(*tasks)
