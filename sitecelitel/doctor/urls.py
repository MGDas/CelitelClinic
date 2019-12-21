from django.urls import path, include
from django.views.decorators.cache import cache_page

from doctor.views_list.views import DoctorListView
from doctor.views_list.views import DoctorDetailView
from doctor.views_list.views import get_filter_doctors_data

from doctor.views_list.view_sets import DoctorViewSet

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('all', DoctorViewSet, basename='doctors_api')

urlpatterns = [
    path('', cache_page(600)(DoctorListView.as_view()), name='doctor_list_url'),
    path('<int:pk>/', DoctorDetailView.as_view(), name='doctor_detail_url'),
    path('filter_docktors/', get_filter_doctors_data, name='get_filter_doctors_data'),
    path('api/v0/', include(router.urls)),
]
