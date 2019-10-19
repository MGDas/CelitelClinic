from django.db import models
from clinic.models import BaseModel

# Create your models here.
class ArticleTag(BaseModel):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    header = models.BooleanField(default=True, verbose_name='Показать в шапке')

    class Meta:
        db_table = "articletag"

    def __str__(self):
        return self.title


class DoctorTag(BaseModel):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    header = models.BooleanField(default=True, verbose_name='Показать в шапке')

    class Meta:
        db_table = "doctortag"

    def __str__(self):
        return self.title
