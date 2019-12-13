from django.core.management.base import BaseCommand
from service.models import Price, Service, ServiceGroup, PriceType


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        PriceType.objects.all().delete()
        print("All PriceType is deleted!!!")
        Price.objects.all().delete()
        print("All Price is deleted!!!")
        Service.objects.all().delete()
        print("All Services is deleted!!!")
        ServiceGroup.objects.all().delete()
        print("All ServiceGroup is deleted!!!")
