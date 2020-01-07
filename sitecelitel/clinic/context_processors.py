from article.models import Article
from tag.models import ArticleTag
from promotion.models import Promotion
from service.models import ServiceGroup
from rusdoc.models import RussianDoctor
from organization.models import Organization


def index(request):
    articles_header = Article.pub_objects.all().order_by('-updated')[:2]
    articles_tags = ArticleTag.objects.all().order_by('-id')[:6]
    rus_doc = RussianDoctor.pub_objects.filter(header=True).order_by('-updated')[:3]

    organizations = {}
    organ_cities = [organ for organ in Organization.pub_objects.values_list('city', flat=True).distinct() if organ]
    for city in organ_cities:
        if city:
            organizations[city] = Organization.objects.filter(city=city, public=1).values_list('id', 'name', 'address', 'operating_mode', 'image')

    service_groups = ServiceGroup.pub_objects.all()

    return {
        "rus_doc": rus_doc,
        "articles_header": articles_header,
        "articles_tags": articles_tags,
        "service_groups": service_groups,
        'organ_cities': organ_cities,
        'organizations': organizations
        }
