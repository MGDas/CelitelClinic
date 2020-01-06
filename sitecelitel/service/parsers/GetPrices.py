import requests
import asyncio
import logging
from service.models import Price, PriceType, Service

def connect(url):

    response = requests.get(url)
    return response.json()

async def save_in_db(service_id, price_id, price):

    try:
        price_id = PriceType.objects.get(code=price_id)
    except PriceType.DoesNotExist as e:
        price_id = False

    try:
        service_id = Service.objects.get(code=service_id)
    except Service.DoesNotExist as e:
        service_id = False

    if price_id and service_id and price:
        update_field = {'price': int(price)}
        service, status = Price.objects.update_or_create(
            service=service_id,
            price_type=price_id,
            defaults=update_field
        )
        if not status:
            print(f'{service}...{service.price_type}... цена ОБНОВЛЕНА!')
        else:
            print(f'{service}...{service.price_type}... цена СОЗДАНА!')

async def main():
    url = 'https://celitel05.ru/json/GetPrices.json'
    data = connect(url)

    tasks = []

    for d in data:
        task = asyncio.create_task(save_in_db(d['service_id'], d['price_id'], d['price']))
        tasks.append(task)

    await asyncio.gather(*tasks)
