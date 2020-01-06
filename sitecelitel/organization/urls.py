from django.urls import path
from organization.views import OrganDetailView


urlpatterns = [
    path('<int:pk>/', OrganDetailView.as_view(), name='organ_detail_url'),
]
