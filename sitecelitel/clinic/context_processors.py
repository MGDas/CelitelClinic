from article.models import Article
from tag.models import ArticleTag

def index(request):
    articles_header = Article.objects.all().order_by('-id')[:2]
    articles_tags = ArticleTag.objects.all().order_by('-id')[:6]
    return {
        "articles_header": articles_header,
        "articles_tags": articles_tags,
        }
