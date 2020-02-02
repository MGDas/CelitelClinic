from django.urls import path, include
from organization.routers import router

from organization.views import views

urlpatterns = [
    path('<int:pk>/', views.OrganDetailView.as_view(), name='organ_detail_url'),
    path('api/v0/', include(router.urls))
]
