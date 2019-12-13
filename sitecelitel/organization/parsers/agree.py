import asyncio
import requests
from organization.models import Organization, Agreement
from service.models import PriceType

def connect():

    response = requests.get('https://celitel05.ru/json/GetAgreements.json')
    return response.json()

async def save_in_db(code, name, organ_code, price_type):

    try:
        organ_id = Organization.objects.only('id').get(code=organ_code)
    except Organization.DoesNotExist:
        organ_id = None

    try:
        price_id = PriceType.objects.only('id').get(code=price_type)
    except PriceType.DoesNotExist:
        price_id = None

    agree, status = Agreement.objects.update_or_create(
        code=code,
        defaults={
            'code': code,
            'name': name
        }
    )

    if organ_id:
        agree.organization_id = organ_id
    if price_id:
        agree.price_id = price_id
    agree.save()

    if status:
        print(f"{agree}...................СОЗДАНО!")
    else:
        print(f"{agree}...................ОБНОВЛЕНО!")

async def main():

    data = connect()
    tasks = []

    for d in data:
        task = asyncio.create_task(save_in_db(d['code'], d['name'], d['organization_id'], d['price_id']))
        tasks.append(task)

    await asyncio.gather(*tasks)
