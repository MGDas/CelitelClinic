from django.db import models
from clinic.models import BaseModel

def create_name():
    pass

class RussianDoctor(BaseModel):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    preview = models.TextField(blank=True, verbose_name='Превью')
    image = models.ImageField(upload_to=create_name, blank=True, verbose_name='Изображение')
    reception = models.BooleanField(default=True, verbose_name='Приём')

    class Meta:
        db_table = 'russian_doctors'
        verbose_name = 'Российский врач'
        verbose_name_plural = 'Российские врачи'

    def __str__(self):
        return self.title
