from rest_framework import serializers
from doctor.models import Doctor, DoctorTiming, Timing
from organization.models import Organization, Department, Agreement
from service.models import Service


class AgreementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Agreement
        fields = ['code']


class OrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = ['id', 'name', 'address', 'agreement']

    agreement = serializers.SerializerMethodField()

    def get_agreement(self, organ):
        try:
            agree = organ.agreement.only('code').all().values_list('code', flat=True)[0]
        except:
            agree = ''
        return agree


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
            'id', 'full_name', 'avatar', 'academic_degree', 'experience', 'url', 'department', 'dates', 'services', 'code')


class DoctorListSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(many=True)
    dates = DoctorTimingSerializer(many=True)
    services = ServiceSerializer(many=True)

    class Meta:
        model = Doctor
        fields = ('id', 'full_name', 'department', 'dates', 'services')
