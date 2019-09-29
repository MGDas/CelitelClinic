from django.db import models

class BaseModel(models.Model):
    public = models.BooleanField(default=True, verbose_name='Публикация')

    class Meta:
        abstract = True
