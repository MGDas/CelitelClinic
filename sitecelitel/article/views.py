import random
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic import DetailView
from article.models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'article/article_list.html'
    context_object_name = "articles"

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article/article_detail.html'
    context_object_name = "article"
    paginator_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['other_articles'] = Article.objects.all()[:4]

        id = random.choice(Article.objects.filter(public=True).values_list('id', flat=True))
        context['next_page'] = Article.objects.get(id=id)
        return context
