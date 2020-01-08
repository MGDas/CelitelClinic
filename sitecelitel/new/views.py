from django.views.generic import ListView, DetailView
from django.shortcuts import render
from new.models import New



class NewListView(ListView):
    model = New
    template_name = 'new/new_list.html'
    context_object_name = "news"
    queryset = New.pub_objects.all().order_by('-updated')
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['years'] = list(reversed(New.pub_objects.values_list('updated__year', flat=True).distinct()))
        return context


class NewListViewYear(ListView):
    model = New
    template_name = 'new/new_list_year.html'
    context_object_name = 'news'
    paginate_by = 8

    def get_queryset(self):
        queryset = New.pub_objects.filter(updated__year=self.kwargs['year']).order_by('-updated')
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['news_dates'] = list(reversed(New.pub_objects.values_list('updated__year', flat=True).distinct()))
        return context


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
