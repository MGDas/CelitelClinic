from rest_framework import routers
from rest_framework.routers import DefaultRouter

from organization.views import view_sets


router = routers.DefaultRouter()
router.register('doctors', view_sets.OrganDoctorViewSet, basename='organ_doctor_api')
router.register('organs', view_sets.OrganViewSet, base_name='organs_api')
