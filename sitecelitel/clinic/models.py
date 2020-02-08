from django.db import models
from django.conf import settings
from django.utils import timezone

from clinic.utils import get_image_pc, get_image_mob, get_image_partner


class PublicManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(public=True)


class PublicModel(models.Model):

    public = models.BooleanField(default=True, verbose_name='Публикация')

    objects = models.Manager()
    pub_objects = PublicManager()

    class Meta:
        abstract = True


class BaseModel(PublicModel):

    created = models.DateField(default=timezone.now, verbose_name='Дата создания')
    updated = models.DateField(default=timezone.now, verbose_name='Дата обновления')

    class Meta:
        abstract = True


class Slider(PublicModel):

    title = models.CharField(max_length=500, verbose_name='Название')
    url = models.CharField(max_length=500, blank=True, help_text='Пример: /article/about/', verbose_name='URL')
    image_pc = models.ImageField(upload_to=get_image_pc, blank=True, verbose_name='Изображение')
    image_mob = models.ImageField(upload_to=get_image_mob, blank=True, verbose_name='Изображение моб.')
    order = models.PositiveIntegerField(default=0, blank=True, verbose_name='Сортировка')

    class Meta:
        db_table = 'sliders'
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайдер'
        ordering = ['-order']

    def save(self, *args, **kwargs):
        if not self.order:
            self.order = self.id
        return super().save(*args, **kwargs)

    @property
    def get_current_site(self):
        return "/".join(['http:/', settings.SITE[0].strip('/'), self.url.strip('/')])

    def __str__(self):
        return self.title[:50]


class Partner(PublicModel):

    name = models.CharField(max_length=500, db_index=True, verbose_name='Название')
    url = models.URLField(verbose_name='URL')
    logo = models.FileField(upload_to=get_image_partner, verbose_name='logo')
    order = models.PositiveIntegerField(default=0, blank=True, verbose_name='Сортировка')

    class Meta:
        db_table = 'partners'
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'
        ordering = ['-order']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.order:
            self.order = self.id
        return super().save(*args, **kwargs)


class Hospital(PublicModel):
    title = models.CharField(max_length=500, verbose_name='Название')
    url = models.CharField(max_length=500, blank=True, verbose_name='URL')
    image_one = models.ImageField(upload_to=get_image_pc, blank=True, verbose_name='Изображение для шапки 1')
    image_two = models.ImageField(upload_to=get_image_pc, blank=True, verbose_name='Изображение для шапки 2')
    image_three = models.ImageField(upload_to=get_image_pc, blank=True, verbose_name='Изображение для шапки 3')
    description = models.TextField(blank=True, verbose_name='Текст на шапке')
    content = models.TextField(blank=True, verbose_name='Текст')
    
    image_full = models.ImageField(upload_to=get_image_pc, blank=True, verbose_name='Изображение для страницы')

    class Meta:
        db_table = 'hospital'
        verbose_name = 'Стационар'
        verbose_name_plural = 'Стационар'
        ordering = ['-title']