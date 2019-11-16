import asyncio
from time import time
from django.core.management.base import BaseCommand
from doctor.parsers.GetSpecialization import main as special

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        start = time()
        asyncio.run(special())
        end = time()

        print(end - start)