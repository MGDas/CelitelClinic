from article.models import Article
from tag.models import ArticleTag
from promotion.models import Promotion
from service.models import ServiceGroup
from clinic.utils import get_service_group_to_alphabet

def index(request):
    articles_header = Article.pub_objects.all().order_by('-updated')[:2]
    articles_tags = ArticleTag.objects.all().order_by('-id')[:6]
    promotion_header = Promotion.pub_objects.filter(header=True).order_by('-updated')[:3]

    service_groups = get_service_group_to_alphabet()

    return {
        "promotion_header": promotion_header,
        "articles_header": articles_header,
        "articles_tags": articles_tags,
        "service_groups": service_groups,
        }
