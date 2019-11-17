import requests
import logging
from service.models import PriceType

def connect(url):

    response = requests.get(url)
    return response.json()

def save_in_db(code, name):

    update_field = {'name': name}
    group, status = PriceType.objects.update_or_create(code=code, defaults=update_field)
    if not status:
        print(f'{group}.... цена ОБНОВЛЕНА!')
    else:
        print(f'{group}.... цена СОЗДАНА!')

def main():
    url = 'http://test.studiovector.art/json/GetPriceTypes.json'
    data = connect(url)

    for d in data:
        save_in_db(d['code'], d['name'])
