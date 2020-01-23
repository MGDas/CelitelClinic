from doctor.models import Doctor, Specialization, Timing, DoctorTiming
from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def handle(self, *args, **kwargs):

 #       Doctor.objects.all().delete()
 #       print("УСПЕШНО — удалены с сайта Доктора")
        Specialization.objects.all().delete()
        print("УСПЕШНО — удалены с сайта Специализации")
        Timing.objects.all().delete()
        print("УСПЕШНО — удалены с сайта Часы приема!")
        DoctorTiming.objects.all().delete()
        print("УСПЕШНО — удалены с сайта Дни приема!")
        print("===================")
#       print("На это ушло: ", end - start)
