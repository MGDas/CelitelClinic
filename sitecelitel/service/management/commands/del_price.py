from django.core.management.base import BaseCommand
from service.models import Price


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        Price.objects.all().delete()
        print("All prices is deleted!!!")