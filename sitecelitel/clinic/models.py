from django.db import models
from django.utils import timezone

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
