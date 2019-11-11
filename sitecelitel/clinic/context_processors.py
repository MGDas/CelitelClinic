from article.models import Article
from tag.models import ArticleTag
from promotion.models import Promotion

def index(request):
    articles_header = Article.pub_objects.all().order_by('-updated')[:2]
    articles_tags = ArticleTag.objects.all().order_by('-id')[:6]
    promotion_header = Promotion.pub_objects.filter(header=True).order_by('-updated')[:3]

    return {
        "promotion_header": promotion_header,
        "articles_header": articles_header,
        "articles_tags": articles_tags,
        }
