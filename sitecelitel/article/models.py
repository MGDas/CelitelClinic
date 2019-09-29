from django.db import models
from clinic.models import BaseModel

def create_name():
    pass


class Article(BaseModel):
    doctor = models.ManyToManyField("doctor.Doctor", related_name='article', verbose_name='Доктор')

    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='Уникальное имя')

    preview = models.TextField(blank=True, null=True, verbose_name='Превью')    # Редактор
    content = models.TextField(blank=True, null=True, verbose_name='Контент')   # Редактор

    created = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)
    image = models.ImageField(upload_to=create_name, blank=True, verbose_name='Изображение')

    class Meta:
        db_table = 'article'
        verbose_name_plural = 'Статьи'
        verbose_name = 'Статья'

    def __str__(self):
        return self.title


class Rating(models.Model):
    article = models.OneToOneField(Article, on_delete=models.CASCADE, related_name='rating')
    like = models.PositiveIntegerField(default=0)
    dislike = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'rating'
