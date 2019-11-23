from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from service.models import ServiceGroup



class ServiceGroupDetailView(DetailView):
    model = ServiceGroup
    template_name = 'service/service_detail.html'
    context_object_name = 'service_group'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = self.object.services.filter(public=True)
        return context
