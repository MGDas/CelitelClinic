from django.views.generic import ListView
from faq.models import Faq
from clinic.models import Hospital


class FaqViewList(ListView):
    template_name = 'faq/faq_list.html'
    queryset = Faq.pub_objects.all()
    context_object_name = 'faqs'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hospital'] = Hospital.objects.all()[0]
        return context
