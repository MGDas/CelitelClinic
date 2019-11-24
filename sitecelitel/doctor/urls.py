from django.urls import path
from django.views.decorators.cache import cache_page
from doctor.views import DoctorListView
from doctor.views import DoctorDetailView

urlpatterns = [
    path('', cache_page(600)(DoctorListView.as_view()), name='doctor_list_url'),
    path('<int:pk>/', DoctorDetailView.as_view(), name='doctor_detail_url'),
]
