from doctor.models import Doctor
from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        Doctor.objects.all().delete()
        print('Deleted Specializations!!!')
