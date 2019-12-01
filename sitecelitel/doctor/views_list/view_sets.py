from rest_framework.viewsets import ModelViewSet
from doctor.models import Doctor
from doctor.serializers import DoctorListSerializer


class DoctorViewSet(ModelViewSet):
    serializer_class = DoctorListSerializer

    def get_queryset(self):
        print()
        print(self.request)
        print()
        return Doctor.pub_objects.all()
