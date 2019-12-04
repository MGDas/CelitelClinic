from django.core.management.base import BaseCommand
from service.models import Price, Service


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        Service.objects.all().delete()
        print("All prices is deleted!!!")
