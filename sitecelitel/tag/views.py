from django.views.generic import DetailView
from tag.models import ArticleTag
from tag.models import DoctorTag
from clinic.models import Hospital


class ArticleTagDetailView(DetailView):
    model = ArticleTag
    template_name = 'tag/article_tags.html'
    context_object_name = "article_tag"
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['hospital'] = Hospital.objects.all()[0]
        return context


class DoctorTagDetailView(DetailView):
    model = DoctorTag
    template_name = 'tag/doctor_tag.html'
    context_object_name = "tag_doctor"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['hospital'] = Hospital.objects.all()[0]
        return context