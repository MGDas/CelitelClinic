from article.models import Article
from tag.models import ArticleTag
from tag.models import DoctorTag
from doctor.models import Doctor
from rusdoc.models import RussianDoctor
from service.models import ServiceGroup
from organization.models import Organization

from django.utils import timezone

def index(request):
    articles_header = Article.pub_objects.all().order_by('-updated')[:2]
    articles_tags = ArticleTag.objects.only("id", "title").order_by('-id')[:6]
    doctors_tags = DoctorTag.pub_objects.only("id", "title").filter(header=True).order_by('-id')[:6]
    rus_doc = RussianDoctor.pub_objects.only("pk", "title", "image").filter(header=True).filter(data_end__gt=timezone.now()).order_by('created')[:3]
    best_doctor = Doctor.pub_objects.only("avatar", "full_name", "specialization").filter(the_best=True).first()

    organizations = {}
    organ_cities = [organ for organ in Organization.pub_objects.values_list('city', flat=True).distinct() if organ]
    for city in organ_cities:
        if city:
            organizations[city] = Organization.objects.only('id', 'name', 'address', 'operating_mode', 'image_mobile').filter(city=city, public=1).values_list('id', 'name', 'address', 'operating_mode', 'image_mobile')

    service_groups = ServiceGroup.pub_objects.all()

    return {
        "rus_doc": rus_doc,
        "articles_header": articles_header,
        "articles_tags": articles_tags,
        "doctors_tags": doctors_tags,
        "service_groups": service_groups,
        'organ_cities': organ_cities,
        'organizations': organizations,
        'best_doctor': best_doctor
    }
