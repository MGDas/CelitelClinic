from django.urls import path

from doctor.views import DoctorListView
from doctor.views import DoctorDetailView

urlpatterns = [
    path('', DoctorListView.as_view(), name='doctor_list_url'),
    path('<int:pk>/', DoctorDetailView.as_view(), name='doctor_detail_url'),
]
