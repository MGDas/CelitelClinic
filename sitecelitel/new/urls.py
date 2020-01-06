from django.urls import path
from new.views import (
    NewListViewYear,
    NewListView, NewDetailView,
    # NewListViewMonth, NewListViewDay,
)

urlpatterns = [
    path('', NewListView.as_view(), name='news_list_url'),
    path('<year>/', NewListViewYear.as_view(), name='news_list_year_url'),
    path('<year>/<month>/<day>/<pk>/', NewDetailView.as_view(), name='news_detail_url'),
]
