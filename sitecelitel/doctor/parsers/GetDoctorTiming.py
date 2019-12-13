import asyncio
import requests
import json
import os

from datetime import datetime

from doctor.models import DoctorTiming, Doctor, Timing
from organization.models import Department

path_to = os.path.dirname(__file__)

def connect(url):
    response = requests.get(url)
    return response.json()


def date_comparison(date_reception):

    date_reception = datetime.strptime(date_reception, '%Y-%m-%d')
    date_now = datetime.strptime(str(datetime.now(tz=None).date()), '%Y-%m-%d')

    if date_reception < date_now:
        return False
    return True


async def save_db(doc_code, depart_code, days):

    try:
        doctor = Doctor.objects.get(code=doc_code)
    except:
        doctor = False

    try:
        depart_code = Department.objects.get(code=depart_code).organization
    except:
        depart_code = False

    if days and doctor and depart_code:
        print(f"Create for {doc_code}")
        for day in days:
            if not date_comparison(day['dt']):
                continue

            date, status = DoctorTiming.objects.update_or_create(
                doctor=doctor,
                organization=depart_code, # fix
                date=day['dt']
            )
            print(f"----------{day['dt']}")

            if not day['shedule']:
                continue

            for time in day['shedule']:
                time_reception = Timing.objects.update_or_create(
                    date=date,
                    start=time['time_start'],
                    end=time['time_end'],
                    free=time['free']
                )
                print(f"----------------------------{time['time_start']}")


async def main():
    data = connect("https://celitel05.ru/json/GetDoctorsDays.json")
    
    tasks = []

    for d in data:
        task = asyncio.create_task(save_db(d['code'], d['department_id'], d['days']))
        tasks.append(task)

    await asyncio.gather(*tasks)
