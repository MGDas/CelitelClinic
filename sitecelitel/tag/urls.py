from django.urls import path
from tag.views import ArticleTagDetailView
from tag.views import DoctorTagDetailView


urlpatterns = [
    path('articles/<str:slug>/', ArticleTagDetailView.as_view(), name='article_tags_detail_url'),
    path('doctors/<str:slug>/', DoctorTagDetailView.as_view(), name='doctor_tags_detail_url')
]
