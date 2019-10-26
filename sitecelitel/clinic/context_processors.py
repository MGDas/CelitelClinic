from article.models import Article
from tag.models import ArticleTag
from new.models import New

def index(request):
    articles_header = Article.pub_objects.all().order_by('-id')[:2]
    articles_tags = ArticleTag.objects.all().order_by('-id')[:6]
    news_header = New.pub_objects.filter(header=True).order_by('-updated')[:3]
    return {
        "news_header": news_header,
        "articles_header": articles_header,
        "articles_tags": articles_tags,
        }
