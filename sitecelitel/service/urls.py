from django.urls import path
from service.views import ServiceGroupDetailView

urlpatterns = [
    path('<int:pk>/', ServiceGroupDetailView.as_view(), name='service_detail_url')
]
