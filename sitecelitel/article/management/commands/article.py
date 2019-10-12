from django.core.management.base import BaseCommand
from article.models import Article
from slugify import slugify
from django.conf import settings
import os

DIR_NAME = os.path.dirname(os.path.dirname(__file__))

def write_file(file):
    with open(f'{DIR_NAME}/examples/articles/lorems/{file}', 'r') as file:
        return file.read()

class Command(BaseCommand):

    help = 'Add article without autor.'

    def handle(self, *args, **kwrags):

        for i in range(10):
            title = f'Интимная жизнь в молодости: проблемы и решения #{i}.'

            article = Article.objects.create(
                title=title,
                caption='Мисак Владимирович',
                slug=slugify(title),
                preview=write_file('preview.txt'),
                content=write_file('content.txt'),
                image=os.path.join(settings.MEDIA_URL, '/articles/doctor.jpg'),
            )
            article.save()
            print(f"Article #{i} created!")
