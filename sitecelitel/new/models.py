from django.db import models
from django.shortcuts import reverse
from clinic.models import BaseModel, PublicManager
from sitecelitel.utils import get_photo

class New(BaseModel):

    title = models.CharField(max_length=255, verbose_name='Заголовок')
    preview = models.TextField(verbose_name='Превью')
    content = models.TextField(verbose_name='Контент')
    image = models.ImageField(upload_to=get_photo, blank=True, verbose_name='Изображение')
    caption = models.CharField(max_length=255, blank=True, verbose_name='Подпись')

    header = models.BooleanField(default=True, verbose_name='Показать в шапке')

    doctors = models.ManyToManyField(
        "doctor.Doctor",
        related_name='news',
        blank=True,
        verbose_name='Доктора'
    )

    class Meta:
        db_table = 'news'
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_detail_url', kwargs={
            'year': self.updated.year,
            'month': self.updated.strftime('%m'),
            'day': self.updated.strftime('%d'),
            'pk': self.pk
        })
