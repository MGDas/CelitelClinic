from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from doctor.models import Doctor
from doctor.serializers import DoctorListSerializer


class DoctorViewSet(ModelViewSet):
    serializer_class = DoctorListSerializer
    filter_beckend = [DjangoFilterBackend]
    search_fields = ['name', 'code']
    queryset = Doctor.pub_objects.all()
