import asyncio
import requests
from doctor.models import Specialization

def connect(url):
    response = requests.get(url)
    return response.json()

def save_in_db(code, name):

    special, status = Specialization.objects.update_or_create(
        code=code,
        name=name
    )

    if not status:
        print(f"{special}......ОБНОВЛЕНО!")
    else:
        print(f"{special}......СОЗДАНО!")

def main():

    url = 'https://celitel05.ru/json/GetSpecialization.json'
    data = connect(url)

    count = 0
    for d in data:
        save_in_db(d['code'], d['name'])
        count += 1

    print("============================")
    print(f"Specialization saved. Count {count}.")
    print("============================")
