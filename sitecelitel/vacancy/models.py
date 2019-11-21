from django.db import models
from clinic.models import BaseModel

class Group(BaseModel):
    title = models.CharField(max_length=100, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'groups_vacancies'
        verbose_name = 'Группа вакансии'
        verbose_name_plural = 'Группы вакансий'


class Vacancy(BaseModel):
    group = models.ForeignKey(
        Group,
        on_delete=models.DO_NOTHING,
        null=True,
        related_name='vacancies',
        verbose_name='Группа'
    )
    city = models.CharField(max_length=255, verbose_name='Город')
    position = models.CharField(max_length=255, verbose_name='Позиция')
    content = models.TextField(blank=True, verbose_name='Контент')
    phone = models.CharField(max_length=45, blank=True, verbose_name='Телефон')
    email = models.CharField(max_length=45, blank=True, verbose_name='Email')

    class Meta:
        db_table = 'vacancies'
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return self.position
