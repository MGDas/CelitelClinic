from django.urls import path
from tag.views import ArticleTagDetailView

urlpatterns = [
    path('<str:slug>/', ArticleTagDetailView.as_view(), name='article_tags_detail_url'),
]
