from django.urls import path, include
from clinic.views import IndexView


urlpatterns = [
    path('', IndexView.as_view(), name='index_url'),
    path('articles/', include('article.urls')),
]
