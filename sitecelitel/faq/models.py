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
        if len(self.question) > 60:
            return f"({self.id}) {self.question[:60]}..."
        return f"({self.id}) {self.question}"

    def save(self, *args, **kwargs):
        self.public = True if self.answer else False
        super().save(*args, **kwargs)
