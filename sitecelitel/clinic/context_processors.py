from article.models import Article
from tag.models import ArticleTag
from new.models import New

def index(request):
    articles_header = Article.objects.all().order_by('-id')[:2]
    articles_tags = ArticleTag.objects.all().order_by('-id')[:6]
    news_header = New.objects.all().order_by('-updated')[:3]
    return {
        "news_header": news_header,
        "articles_header": articles_header,
        "articles_tags": articles_tags,
        }
