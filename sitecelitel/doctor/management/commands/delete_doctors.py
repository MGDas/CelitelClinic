from doctor.models import Doctor, Specialization, Timing, DoctorTiming
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        # Doctor.objects.all().delete()
        Specialization.objects.all().delete()
        print("Specializations deleted!")
        Timing.objects.all().delete()
        print("Timings deleted!")
        DoctorTiming.objects.all().delete()
        print("DoctorTimings deleted!")
        print("===================")
        print("===================")
        print("===================")
        print("===================")
