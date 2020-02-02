from django.views.generic import DetailView
from tag.models import ArticleTag
from tag.models import DoctorTag


class ArticleTagDetailView(DetailView):
    model = ArticleTag
    template_name = 'tag/article_tags.html'
    context_object_name = "article_tag"


class DoctorTagDetailView(DetailView):
    model = DoctorTag
    template_name = 'tag/doctor_tag.html'
    context_object_name = "tag_doctor"
