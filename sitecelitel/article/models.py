from django.db import models
from clinic.models import BaseModel
from sitecelitel.utils import get_photo

class Article(BaseModel):
    doctor = models.ForeignKey(
        "doctor.Doctor",
        on_delete=models.SET_NULL,
        null=True,
        related_name='article',
        blank=True,
        verbose_name='Доктор'
    )

    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='Уникальное имя')

    preview = models.TextField(blank=True, verbose_name='Превью')               # Редактор
    content = models.TextField(blank=True, verbose_name='Контент')              # Редактор
    caption = models.CharField(max_length=250, blank=True, verbose_name='Подпись')

    image = models.ImageField(upload_to=get_photo, blank=True, verbose_name='Изображение')
    created = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)

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
