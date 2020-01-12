from django.db import models
from django.conf import settings
from django.utils import timezone

from clinic.utils import get_image_pc, get_image_mob


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
        return self.url
