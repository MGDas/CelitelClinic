from django.urls import path
from vacancy.views import VacancyListView, VacancyCityListView

urlpatterns = [
    path('', VacancyListView.as_view(), name='vacancy_list_url'),
    path('<str:city>/', VacancyCityListView.as_view(), name='vacancy_in_city_url')
]
