from django.core.management.base import BaseCommand
from article.models import Article

class Command(BaseCommand):

    help = 'Delete article without autor.'

    def handle(self, *args, **kwrags):

        try:
            Article.objects.filter(doctor=None).delete()
            print(f"Article deleted!")
        except:
            print("Not articles!")
