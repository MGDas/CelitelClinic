from django.urls import path, include
from rest_framework.routers import DefaultRouter

from organization.views import views
from organization.views import view_sets


router = DefaultRouter()
router.register('doctors', view_sets.OrganDoctorViewSet, basename='organ_doctor_api')

urlpatterns = [
    path('<int:pk>/', views.OrganDetailView.as_view(), name='organ_detail_url'),
    path('api/v0/', include(router.urls))
]
