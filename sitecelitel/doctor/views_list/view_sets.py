from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q

from doctor.models import Doctor, Specialization
from organization.models import Organization, Department
from doctor.serializers import OrderSerializer


class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    filter_beckend = [DjangoFilterBackend]

    def get_queryset(self):

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
            return Doctor.pub_objects.filter(*result)

        return Doctor.pub_objects.all()[:3]
