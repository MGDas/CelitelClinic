import asyncio
from time import time
from django.core.management.base import BaseCommand
from organization.parsers.load_organ import main as loader

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        start = time()
        asyncio.run(loader())
        end = time()

        print(end - start)
