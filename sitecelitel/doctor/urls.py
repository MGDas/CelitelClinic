from django.urls import path, include
from django.views.decorators.cache import cache_page

from doctor.views_list.views import DoctorListView
from doctor.views_list.views import DoctorDetailView
from doctor.views_list.views import OrderView

from doctor.views_list.view_sets import DoctorViewSet
from doctor.views_list.view_sets import OrderViewSet

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('all', DoctorViewSet, basename='doctors_api')
router.register('order', OrderViewSet, basename='order_api')

urlpatterns = [
    path('', cache_page(600)(DoctorListView.as_view()), name='doctor_list_url'),
    path('order/', OrderView.as_view(), name='order_url'),
    path('<int:pk>/', DoctorDetailView.as_view(), name='doctor_detail_url'),
    path('api/v0/', include(router.urls)),
]
