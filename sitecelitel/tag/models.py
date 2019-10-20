from django.db import models
from clinic.models import BaseModel

# Create your models here.
class ArticleTag(BaseModel):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='Уникальное имя')
    header = models.BooleanField(default=True, verbose_name='Показать в шапке')

    class Meta:
        db_table = "articletag"
        verbose_name = 'Тег статьи'
        verbose_name_plural = 'Теги статей'

    def __str__(self):
        return self.title


class DoctorTag(BaseModel):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='Уникальное имя')
    header = models.BooleanField(default=True, verbose_name='Показать в шапке')

    class Meta:
        db_table = "doctortag"
        verbose_name = 'Тег доктора'
        verbose_name_plural = 'Теги докторов'

    def __str__(self):
        return self.title
