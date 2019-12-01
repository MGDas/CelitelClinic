from django.db import models
from django.shortcuts import reverse
from clinic.models import BaseModel


class Promotion(BaseModel):
    title = models.CharField(max_length=255, verbose_name='Название')
    preview = models.TextField(blank=True, verbose_name='Превью')
    content = models.TextField(blank=True, verbose_name='Контент')

    note = models.CharField(max_length=255, blank=True, null=True, verbose_name='Примечание')

    data_start = models.DateField(blank=True, verbose_name='Дата начала')
    data_end = models.DateField(blank=True, verbose_name='Дата конца')

    header = models.BooleanField(default=True, verbose_name='Показать в шапке')

    doctor = models.ManyToManyField(
        "doctor.Doctor",
        blank=True,
        related_name='promotions',
        verbose_name='Доктор',
    )

    class Meta:
        db_table = 'promotions'
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'
        ordering = ["-created"]

    def __str__(self):
        return self.title

    def get_absolute_url(self, **kwargs):
        return reverse('promotion_detail_url', kwargs={'pk': self.pk})
