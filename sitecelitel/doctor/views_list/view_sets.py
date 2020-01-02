from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q

from doctor.models import Doctor
from doctor.serializers import DoctorListSerializer
from doctor.serializers import OrderSerializer


class DoctorViewSet(ModelViewSet):
    serializer_class = DoctorListSerializer
    filter_beckend = [DjangoFilterBackend]
    search_fields = ['name', 'code']
    queryset = Doctor.pub_objects.all()


class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    filter_beckend = [DjangoFilterBackend]
    queryset = Doctor.pub_objects.all()[:3]

    def get(self, request, *args, **kwargs):

        result = []

        name = self.request.GET.get('orderFiltersName', None)
        spec = self.request.GET.get('orderFiltersSpecialization', None)
        addr = self.request.GET.get('orderFiltersAddress', None)
        child = self.request.GET.get('orderFiltersChild', None)

        if name:
            result.append(Q(full_name__icontains=name))

        if spec:
            specials = Specialization.objects.filter(name__iexact=spec)
            result.append(Q(specialization__in=specials))

        if addr:
            organ = Organization.objects.filter(address__iexact=addr)
            depart = Department.objects.filter(organization__in=organ)
            result.append(Q(department__in=depart))

        if child:
            result.append(Q(childish=True))

        if result:
            return self.queryset.filter(*result)

        return None
