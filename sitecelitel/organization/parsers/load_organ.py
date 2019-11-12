import asyncio
import json
import os
from organization.models import Organization

pwd = os.path.dirname(os.path.dirname(__file__))

async def reader():

    with open(f'{pwd}/files/GetOrganizations.json', 'r') as file:
        return json.load(file)

async def save_in_db(code, name, namefull):

    organ, o = Organization.objects.get_or_create(
        code=code,
        name=name,
        namefull=namefull
    )
    organ.save()
    print(f"{organ}...................{o}")

async def main():

    data = await reader()
    tasks = []

    for d in data:
        task = asyncio.create_task(save_in_db(d['code'], d['name'], d['namefull']))
        tasks.append(task)

    await asyncio.gather(*tasks)
