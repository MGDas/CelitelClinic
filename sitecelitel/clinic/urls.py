from django.urls import path
from clinic.views import IndexView


urlpatterns = [
    path('', IndexView.as_view(), name='index_url')
]
