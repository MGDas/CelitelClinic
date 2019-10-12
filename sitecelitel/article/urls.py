from django.urls import path
from article.views import ArticleListView
from article.views import ArticleDetailView


urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list_url'),
    path('<str:slug>/', ArticleDetailView.as_view(), name='article_detail_url')
]
