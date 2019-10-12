from django.core.management.base import BaseCommand
from article.models import Article

class Command(BaseCommand):

    help = 'Delete article with autor.'

    def handle(self, *args, **kwrags):

        try:
            Article.objects.exclude(doctor=None).delete()
            print(f"Article with autor deleted!")
        except:
            print("Not articles!")
