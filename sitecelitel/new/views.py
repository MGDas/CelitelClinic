from django.views.generic import ListView, DetailView
from django.shortcuts import render
from new.models import New
import random


class NewListView(ListView):
    model = New
    template_name = 'new/new_list.html'
    context_object_name = "news"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['years'] = New.objects.values_list('updated__year', flat=True).distinct()
        return context


class NewListViewYear(ListView):
    model = New
    template_name = 'new/new_list_year.html'

    def get(self, request, year):
        news = New.objects.filter(updated__year=year)
        news_dates = New.objects.values_list('updated__year', flat=True).distinct()
        return render(request, self.template_name, {'news': news, 'news_dates': news_dates})


class NewDetailView(DetailView):
    model = New
    template_name = 'new/new_detail.html'
    context_object_name = 'new'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['other_news'] = New.objects.all()[:4]

        id = random.choice(New.objects.filter(public=True).values_list('id', flat=True))
        context['next_page'] = New.objects.get(id=id)
        return context



    # class NewListViewMonth(ListView):
    #     model = New
    #     template_name = 'new/new_list_month.html'
    #     context_object_name = "news"
    #
    #
    # class NewListViewDay(ListView):
    #     model = New
    #     template_name = 'new/new_list_day.html'
    #     context_object_name = "news"
