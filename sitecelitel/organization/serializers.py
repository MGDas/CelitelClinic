from rest_framework import serializers

from doctor.models import Doctor
from doctor.models import Specialization


class SpecializationSerailizer(serializers.ModelSerializer):

    class Meta:
        model = Specialization
        fields = ('name',)


class OrganDoctorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = (
            'id', 'full_name', 'academic_degree', 'experience',
            'adult', 'childish' ,'specialization'
        )

    specialization = SpecializationSerailizer(many=True)
