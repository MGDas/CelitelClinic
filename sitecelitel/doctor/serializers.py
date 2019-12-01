from rest_framework import serializers
from doctor.models import Doctor, DoctorTiming, Timing


class DoctorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'full_name']
