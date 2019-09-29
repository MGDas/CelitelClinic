from django.db import models
from clinic.models import BaseModel

class Vacancy(BaseModel):
    specialization = models.CharField(max_length=255, verbose_name='Специализация')
    city = models.CharField(max_length=255, verbose_name='Город')
    position = models.CharField(max_length=255, verbose_name='Позиция')
    duty = models.TextField(blank=True, verbose_name='Обязанность')
    requiremen = models.TextField(blank=True, verbose_name='Требование')
    condition = models.TextField(blank=True, verbose_name='Условие')
    phone = models.CharField(max_length=45, blank=True, verbose_name='Телефон')
    email = models.CharField(max_length=45, blank=True, verbose_name='Email')

    class Meta:
        db_table = 'vacancies'
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return self.specialization
