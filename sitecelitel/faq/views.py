from django.views.generic import ListView
from faq.models import Faq


class FaqViewList(ListView):
    template_name = 'faq/faq_list.html'
    queryset = Faq.pub_objects.all()
    context_object_name = 'faqs'
    paginate_by = 10
