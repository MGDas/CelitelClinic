import random
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic import DetailView
from django.views.generic.list import MultipleObjectMixin
from article.models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'article/article_list.html'
    context_object_name = "articles"

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article/article_detail.html'
    context_object_name = "article"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tags = self.object.tags.values_list('title', flat=True)
        context['tags'] = tags
        context['other_articles'] = Article.objects.filter(tags__title__in=tags).exclude(id=self.object.id).distinct()[:4]
        try:
            context['next_page'] = Article.objects.get(id=self.object.id + 1)
        except:
            context['next_page'] = Article.objects.first()
        return context
