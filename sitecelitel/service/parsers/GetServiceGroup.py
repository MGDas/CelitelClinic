import requests
import logging
from service.models import ServiceGroup

def connect(url):

    response = requests.get(url)
    return response.json()

def save_in_db(code, name):

    update_field = {'name': name}
    group, status = ServiceGroup.objects.update_or_create(code=code, defaults=update_field)
    if not status:
        print(f'{group}.... группа ОБНОВЛЕНА!')
    else:
        print(f'{group}.... группа СОЗДАНА!')

def main():
    url = 'https://celitel05.ru/json/GetServiceGroups.json'
    data = connect(url)

    for d in data:
        save_in_db(d['code'], d['name'])
