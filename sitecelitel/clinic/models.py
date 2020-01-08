from django.db import models
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
    url = models.URLField(blank=True, help_text='Пример: http://example.com/about', verbose_name='URL')
    image_pc = models.ImageField(upload_to=get_image_pc, blank=True, verbose_name='Изображение')
    image_mob = models.ImageField(upload_to=get_image_mob, blank=True, verbose_name='Изображение моб.')

    class Meta:
        db_table = 'sliders'
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайдер'

    def __str__(self):
        return self.url
