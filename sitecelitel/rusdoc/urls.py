from django.urls import path
from rusdoc.views import (
    RussianDoctorNowListView,
    RussianDoctorPastListView,
    RussianDoctorDetailView,
)


urlpatterns = [
    path('now/', RussianDoctorNowListView.as_view(), name='rusdoc_list_now_url'),
    path('past/', RussianDoctorPastListView.as_view(), name='rusdoc_list_past_url'),
    path('<int:pk>/', RussianDoctorDetailView.as_view(), name='rusdoc_detail_url')
]
