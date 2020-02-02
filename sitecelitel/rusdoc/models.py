from django.db import models
from clinic.models import BaseModel
from sitecelitel.utils import get_photo


class RussianDoctor(BaseModel):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    note = models.CharField(max_length=100, blank=True, verbose_name='Примечание')
    preview = models.TextField(blank=True, verbose_name='Превью')
    content = models.TextField(verbose_name='Контент')

    image = models.ImageField(upload_to=get_photo, blank=True, verbose_name='Изображение')
    capcha = models.CharField(max_length=50, blank=True, verbose_name='Подпись')

    header = models.BooleanField(default=True, verbose_name='Показать в шапке')

    data_start = models.DateField(verbose_name='Дата начала')
    data_end = models.DateField(verbose_name='Дата конца')

    class Meta:
        db_table = 'russian_doctors'
        verbose_name = 'Российский врач'
        verbose_name_plural = 'Российские врачи'
        ordering = ["-data_start"]

    def __str__(self):
        return self.title
