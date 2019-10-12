import os
from django.core.management.base import BaseCommand
from doctor.models import Doctor

DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        for i in range(1, 11):
            doctor = Doctor.objects.create(
                id = i,
                code = f'000000000{i}',
                full_name = f"DoctorZlo {i}",
                photo = os.path.join(DIR_NAME, 'examples/doctors/images/DoctorZlo.jpg'),
                avatar = os.path.join(DIR_NAME, 'examples/doctors/avatars/DoctorZlo.jpg')
            )
            doctor.save()
            print(f"Doctor Zlo #{i} created!!!")
