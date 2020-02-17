from rest_framework.viewsets import ModelViewSet
from django.db.models import Q

from organization.serializers import OrganDoctorSerializer
from organization.serializers import OrganizationSerializer

from organization.models import Organization

from doctor.models import Doctor
from doctor.models import Specialization


class OrganDoctorViewSet(ModelViewSet):
    serializer_class = OrganDoctorSerializer
    queryset = Doctor.pub_objects.all()[:8]

    def get_queryset(self):
        result = []

        name = self.request.GET.get('orderFiltersName', None)
        spec = self.request.GET.get('orderFiltersSpecialization', None)
        child = self.request.GET.get('orderFiltersChild', None)

        if name:
            result.append(Q(full_name__icontains=name))

        if spec:
            specials = Specialization.objects.filter(name__iexact=spec)
            result.append(Q(specialization__in=specials))

        if child:
            result.append(Q(childish=True))

        if result:
            self.queryset = Doctor.pub_objects.filter(*result)

        return self.queryset


class OrganViewSet(ModelViewSet):
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()


