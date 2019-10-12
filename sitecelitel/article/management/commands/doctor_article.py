from django.core.management.base import BaseCommand
from article.models import Article
from doctor.models import Doctor
from slugify import slugify
from django.conf import settings
import os

DIR_NAME = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))

def write_file(file):
    with open(f'{DIR_NAME}/examples/articles/lorems/{file}', 'r') as file:
        return file.read()

class Command(BaseCommand):

    """Создает 10 статей с авторами. Прежде нужно создать авторов как минимум 10."""

    help = 'Add article with autor.'

    def handle(self, *args, **kwrags):

        doctor_list = []
        for doctor in Doctor.objects.all()[:10]:
            doctor_list.append(doctor)

        for i in range(10):
            title = f'Интимная жизнь в молодости: проблемы и решения #{i}.'

            article = Article.objects.create(
                doctor=doctor_list[i],
                title=title,
                slug=slugify(title),
                preview=write_file('preview.txt'),
                content=write_file('content.txt'),
                image=os.path.join(DIR_NAME, 'examples/doctors/images/DoctorZlo.jpg'),
            )
            article.save()
            print(f"Article #{i} with autor created!")
