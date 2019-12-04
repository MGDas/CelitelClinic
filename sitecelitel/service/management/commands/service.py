import asyncio
from time import time
from django.core.management.base import BaseCommand

from service.parsers.GetServiceGroup import main as groups
from service.parsers.GetService import main as service
from service.parsers.GetPriceTypes import main as price_types
from service.parsers.GetPrices import main as price


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        start = time()
        # groups()
        asyncio.run(service())
        # price_types()
        asyncio.run(price())

        end = time()

        print(end - start)
