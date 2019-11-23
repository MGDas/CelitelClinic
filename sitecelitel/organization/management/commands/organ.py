import asyncio
from time import time
from django.core.management.base import BaseCommand
from organization.parsers.organ import main as organ

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        start = time()
        asyncio.run(organ())
        end = time()

        print(end - start)
