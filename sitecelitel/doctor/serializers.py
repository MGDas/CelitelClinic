from rest_framework import serializers
from doctor.models import Doctor, DoctorTiming, Timing
from organization.models import Organization, Department

class OrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = ['id', 'name', 'address']


class TimingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Timing
        fields = ['hour', 'free']


class DoctorTimingSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer()
    timing = TimingSerializer(many=True)

    class Meta:
        model = DoctorTiming
        fields = ['date', 'organization', 'timing']


class DepartmentSerializer(serializers.ModelSerializer):

    organization = OrganizationSerializer()

    class Meta:
        model = Department
        fields = ['organization']


class DoctorListSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(many=True)
    dates = DoctorTimingSerializer(many=True)

    class Meta:
        model = Doctor
        fields = ['id', 'full_name', 'department', 'dates']
