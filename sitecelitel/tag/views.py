from django.views.generic import DetailView
from tag.models import ArticleTag


class ArticleTagDetailView(DetailView):
    model = ArticleTag
    template_name = 'tag/article_tags.html'
    context_object_name = "article_tag"
