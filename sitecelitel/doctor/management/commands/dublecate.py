from django.core.management.base import BaseCommand
from doctor.models import Doctor


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        count = 0
        doctors = Doctor.objects.all()
        for doctor in doctors:
            other_doctor = Doctor.objects.filter(code=doctor.code).exclude(id=doctor.id)

            if other_doctor:
                other_doctor.delete()
                count += 1

            if doctor.main_code:
                doctor_with_same_main_code = Doctor.objects.filter(main_code=doctor.main_code).exclude(id=doctor.id)

                if doctor_with_same_main_code:
                    doctor_with_same_main_code.delete()
                    count += 1

        print("======================")
        print(f"Delete {count} dublicate doctor")
        print("======================")
