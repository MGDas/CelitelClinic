from rest_framework import serializers
from doctor.models import Doctor, DoctorTiming, Timing
from organization.models import Organization, Department, Agreement
from service.models import Service
import requests
from django.db import connections
connection = connections['default']

class OrganizationSerializer(serializers.ModelSerializer):
    agreement = serializers.SerializerMethodField('getServices')
    
    def getServices(self, Organization):
        organizationID = Organization.id

        cursor = connection.cursor()
        organizationAgreement = cursor.execute("SELECT `code` FROM `agreements` WHERE `organization_id` = {}".format(organizationID))
        if organizationAgreement:
            row = cursor.fetchone()[0]
        else:
            row = ""

        return row

    class Meta:
        model = Organization
        fields = ['id', 'name', 'address', 'agreement']


class TimingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Timing
        fields = ['start', 'end', 'free']


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


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'code', 'name']


class DoctorListSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(many=True)
    dates = DoctorTimingSerializer(many=True)
    services = ServiceSerializer(many=True)

    class Meta:
        model = Doctor
        fields = ('id', 'full_name', 'department', 'dates', 'services')



class OrderSerializer(serializers.ModelSerializer):

    department = DepartmentSerializer(many=True)
    dates = DoctorTimingSerializer(many=True)
    services = ServiceSerializer(many=True)

    url = serializers.SerializerMethodField('getUrl')

    def getUrl(self, doctor):
        return f"/doctors/{doctor.id}"

    class Meta:
        model = Doctor
        fields = (
            'id', 'full_name', 'avatar', 'academic_degree', 'experience', 'url', 'department', 'dates', 'services')
