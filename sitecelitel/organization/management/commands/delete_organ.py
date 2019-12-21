from organization.models import Organization, Agreement, Department
from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        Agreement.objects.all().delete()
        Department.objects.all().delete()
        #Organization.objects.all().delete()
        print('Deleted Agreement and Department!!!')
