from django.db import models
from clinic.models import BaseModel


class Faq(BaseModel):
    question = models.TextField(blank=True, verbose_name='Вопрос')
    answer = models.TextField(blank=True, verbose_name='Ответ')

    class Meta:
        db_table = 'faq'
        verbose_name = 'Faq'
        verbose_name_plural = 'Faqs'

    def __str__(self):
        return f"Faq #{self.id}"

    def save(self, *args, **kwargs):
        self.public = True if self.answer else False
        super().save(*args, **kwargs)
