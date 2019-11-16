import asyncio
from time import time
from django.core.management.base import BaseCommand

from service.parsers.GetServiceGroup import main as groups
from service.parsers.GetService import main as service

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        start = time()
        groups()
        asyncio.run(service())
        end = time()

        print(end - start)
