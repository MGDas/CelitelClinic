from django.db import models
from clinic.models import BaseModel, PublicManager
from sitecelitel.utils import get_photo
from django.utils import timezone

class Article(BaseModel):
    doctor = models.ForeignKey(
        "doctor.Doctor",
        on_delete=models.SET_NULL,
        null=True,
        related_name='articles',
        blank=True,
        verbose_name='Доктор'
    )

    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='Уникальное имя')

    preview = models.TextField(blank=True, verbose_name='Превью')               # Редактор
    content = models.TextField(blank=True, verbose_name='Контент')              # Редактор
    caption = models.CharField(max_length=250, blank=True, verbose_name='Подпись')

    image = models.ImageField(upload_to=get_photo, blank=True, verbose_name='Изображение')
    header = models.BooleanField(default=True, verbose_name='Показать в шапке')

    tags = models.ManyToManyField(
        "tag.ArticleTag",
        blank=True,
        related_name='articles',
        verbose_name='Теги'
    )

    class Meta:
        db_table = 'article'
        verbose_name_plural = 'Статьи'
        verbose_name = 'Статья'
        ordering = ["-created"]

    def __str__(self):
        return self.title


class Rating(models.Model):
    article = models.OneToOneField(Article, on_delete=models.CASCADE, related_name='rating')
    like = models.PositiveIntegerField(default=0)
    dislike = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'rating'


class About(BaseModel):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Контент')

    class Meta:
        db_table = 'about'
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

    def __str__(self):
        return self.title
