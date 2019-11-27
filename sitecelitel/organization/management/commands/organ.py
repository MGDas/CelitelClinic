import asyncio
from time import time
from django.core.management.base import BaseCommand
from organization.parsers.organ import main as organ
from organization.parsers.depart import main as depart
from organization.parsers.agree import main as agree

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        start = time()
        asyncio.run(runner())
        end = time()

        print(end - start)

async def runner():

    await organ()
    await depart()
    await agree()
