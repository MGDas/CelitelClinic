import random
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic import DetailView
from article.models import Article
from article.utils import other_articles


class ArticleListView(ListView):
    model = Article
    template_name = 'article/article_list.html'
    context_object_name = "articles"
    queryset = Article.pub_objects.all()

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article/article_detail.html'
    context_object_name = "article"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tags = self.object.tags.all()
        print(tags)

        context['tags'] = tags
        context['other_articles'] = other_articles(tags, self.object)

        articles = list(Article.pub_objects.all())

        try:
            context['next_page'] = articles[articles.index(self.object) + 1]
        except:
            context['next_page'] = articles[0]
        return context
