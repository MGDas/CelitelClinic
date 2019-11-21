from django.views.generic import ListView
from vacancy.models import Group, Vacancy


class VacancyListView(ListView):
    template_name = 'vacancy/vacancy_list.html'
    queryset = Group.pub_objects.all()
    context_object_name = 'groups'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cities'] = Vacancy.pub_objects.values_list('city', flat=True).distinct()
        return context


class VacancyCityListView(ListView):
    template_name = 'vacancy/vacancy_in_city_list.html'
    context_object_name = 'groups'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cities'] = Vacancy.pub_objects.values_list('city', flat=True).distinct()
        context['title'] = self.kwargs['city']
        return context

    def get_queryset(self):
        groups = {}
        is_group = Group.objects.filter(vacancies__city=self.kwargs['city']).only('title')
        for group in is_group:
            vacancies = Vacancy.pub_objects.filter(group=group, city=self.kwargs['city'])
            groups[group] = vacancies.only('position', 'content', 'phone', 'email')
        return groups
