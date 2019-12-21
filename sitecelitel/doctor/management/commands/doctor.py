import asyncio
from time import time
from django.core.management.base import BaseCommand
from doctor.parsers.GetSpecialization import main as special
from doctor.parsers.GetDoctors import main as doctors
from doctor.parsers.GetDoctorTiming import main as timing

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        start = time()
        asyncio.run(runner())
        end = time()

        print(end - start)

async def runner():

    await special()
    print("Specializations parsed!")
    await doctors()
    print("Doctors parsed!")
    await timing()
    print("Timings parsed!")
    print("===================")
    print("===================")
    print("===================")
    print("===================")
