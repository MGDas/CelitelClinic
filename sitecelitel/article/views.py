import random
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic import DetailView
from article.models import Article, About
from article.utils import other_articles
from clinic.models import Hospital


class ArticleListView(ListView):
    template_name = 'article/article_list.html'
    context_object_name = "articles"
    queryset = Article.pub_objects.all()
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hospital'] = Hospital.objects.all()[0]
        return context


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article/article_detail.html'
    context_object_name = "article"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tags = self.object.tags.all()

        context['tags'] = tags
        context['other_articles'] = other_articles(tags, self.object)
        context['hospital'] = Hospital.objects.all()[0]

        articles = list(Article.pub_objects.all())

        try:
            context['next_page'] = articles[articles.index(self.object) + 1]
        except:
            context['next_page'] = articles[0]
        return context


class AboutTemplateView(TemplateView):
    template_name = 'article/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = About.pub_objects.only('title', 'content').first()
        context['hospital'] = Hospital.objects.all()[0]
        return context
