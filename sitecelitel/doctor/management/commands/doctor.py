import asyncio
from time import time
from django.core.management.base import BaseCommand
from doctor.parsers.GetSpecialization import main as special
from doctor.parsers.GetDoctors import main as doctors
from doctor.parsers.GetDoctorTiming import main as timing

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        start = time()
        runner()
        end = time()

        print(end - start)

def runner():

    special()
    print("===================")
    print("===================")
    print("===================")
    print("УСПЕШНО — Записаны Специализации врачей")
    print("===================")
    print("===================")
    print("===================")
    doctors()
    asyncio.run(timing())
    print("===================")
    print("===================")
    print("===================")
    print("УСПЕШНО — Записаны Графики врачей")
    print("===================")
    print("===================")
    print("===================")
