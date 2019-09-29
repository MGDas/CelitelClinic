from django.db import models
from clinic.models import BaseModel


class Promotion(BaseModel):
    doctor = models.ManyToManyField("doctor.Doctor", blank=True, verbose_name='Доктор')
    title = models.CharField(max_length=255, verbose_name='Название')
    preview = models.TextField(blank=True, verbose_name='Превью')
    content = models.TextField(blank=True, verbose_name='Контент')
    data_start = models.DateField(blank=True, verbose_name='Дата начала')
    data_end = models.DateField(blank=True, verbose_name='Дата конца')
    note = models.CharField(max_length=255, blank=True, null=True, verbose_name='Примечание')

    class Meta:
        db_table = 'promotions'
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'

    def __str__(self):
        return self.title
