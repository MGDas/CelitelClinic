from django.views.generic import ListView, DetailView
from django.shortcuts import render
from new.models import New
import random


class NewListView(ListView):
    model = New
    template_name = 'new/new_list.html'
    context_object_name = "news"
    queryset = New.pub_objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['years'] = New.pub_objects.values_list('updated__year', flat=True).distinct()
        return context


class NewListViewYear(ListView):
    model = New
    template_name = 'new/new_list_year.html'

    def get(self, request, year):
        news = New.pub_objects.filter(updated__year=year)
        news_dates = New.pub_objects.values_list('updated__year', flat=True).distinct()
        return render(request, self.template_name, {'news': news, 'news_dates': news_dates})


class NewDetailView(DetailView):
    model = New
    template_name = 'new/new_detail.html'
    context_object_name = 'new'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        news = list(New.pub_objects.all())
        try:
            context['next_page'] = news[news.index(self.object) + 1]
        except:
            context['next_page'] = New.pub_objects.first()
        return context
