from rest_framework import serializers

from organization.models import Organization
from organization.models import Department

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
            'adult', 'childish', 'specialization'
        )

    specialization = SpecializationSerailizer(many=True)


class DoctorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = (
            'id', 'full_name', 'avatar', 'academic_degree',
            'experience', 'url', 'code'
        )

    url = serializers.SerializerMethodField('getUrl')

    def getUrl(self, doctor):
        return f"/doctors/{doctor.id}"


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = ("code", "name")


class OrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = ("id", "code", "city", "address", "doctors")

    doctors = serializers.SerializerMethodField()

    def get_doctors(self, obj):
        departs = obj.department.only("code").values_list('code')
        doctor_serializer = DoctorSerializer(data=Doctor.objects.filter(department__code__in=departs), many=True)
        doctor_serializer.is_valid()
        return doctor_serializer.data
