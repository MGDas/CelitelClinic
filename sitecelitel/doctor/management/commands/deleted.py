from doctor.models import Doctor, Specialization
from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        Specialization.objects.all().delete()
        Doctor.objects.all().delete()
        print('Deleted Specializations!!!')
