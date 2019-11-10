from django.urls import path, include
from clinic.views import IndexView


urlpatterns = [
    path('', IndexView.as_view(), name='index_url'),
    path('articles/', include('article.urls')),
    path('article-tag/', include('tag.urls')),
    path('doctors/', include('doctor.urls')),
    path('news/', include('new.urls')),
    path('promotions/', include('promotion.urls')),
]
