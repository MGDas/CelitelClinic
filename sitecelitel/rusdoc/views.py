from django.views.generic import ListView
from django.views.generic import DetailView
from django.utils import timezone
from rusdoc.models import RussianDoctor


class RussianDoctorNowListView(ListView):
    template_name = 'rusdoc/rusdoc_list_now.html'
    context_object_name = 'russian_doctors'
    queryset = RussianDoctor.pub_objects.filter(data_end__gt=timezone.now())


class RussianDoctorPastListView(ListView):
    template_name = 'rusdoc/rusdoc_list_past.html'
    context_object_name = 'russian_doctors'
    queryset = RussianDoctor.pub_objects.filter(data_end__lt=timezone.now())


class RussianDoctorDetailView(DetailView):
    model = RussianDoctor
    template_name = 'rusdoc/rusdoc_detail.html'
    context_object_name = 'doc'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        rusdocs = list(RussianDoctor.pub_objects.filter(data_end__gt=timezone.now()))
        print()
        print(rusdocs)
        print()
        try:
            context['next_page'] = rusdocs[rusdocs.index(self.object) + 1]
        except:
            context['next_page'] = rusdocs[0]
        return context
