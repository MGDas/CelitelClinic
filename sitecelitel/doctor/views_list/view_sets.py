from rest_framework.viewsets import ModelViewSet
from doctor.models import Doctor
from doctor.serializers import DoctorListSerializer


class DoctorViewSet(ModelViewSet):
    queryset = Doctor.pub_objects.all()
    serializer_class = DoctorListSerializer
