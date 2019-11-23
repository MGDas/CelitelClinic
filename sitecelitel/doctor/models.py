from django.db import models
from clinic.models import BaseModel
from datetime import datetime
from sitecelitel.utils import get_photo

class Specialization(models.Model):

    """Специализация доктора."""

    code = models.CharField(max_length=36)
    name = models.CharField(max_length=255, verbose_name='Название')

    class Meta:
        db_table = 'specialization'
        verbose_name = 'Специялизация'
        verbose_name_plural = 'Специализации'

    def __str__(self):
        return self.name


class Doctor(BaseModel):

    """Доктор"""

    code = models.CharField(max_length=11)                                      # For 1c. Doctor's code
    main_code = models.CharField(max_length=11, blank=True)

    specialization = models.ForeignKey(
        Specialization,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        related_name='doctor',
        verbose_name='Специализация'
    )

    organization = models.ManyToManyField(
        "organization.Organization",
        related_name='doctors',
        verbose_name='Организация'
    )

    department = models.ManyToManyField(
        'organization.Department',
        blank=True,
        related_name='department',
        verbose_name='Депортамент'
    )

    full_name = models.CharField(max_length=255, blank=True, verbose_name='Полное имя')                         # Name Surname Middle name
    photo = models.ImageField(upload_to=get_photo, blank=True, verbose_name='Фото')               # img, svg,
    avatar = models.ImageField(upload_to=get_photo, blank=True, verbose_name='Аватарка')          # avater docter
    experience = models.CharField(max_length=45, blank=True, verbose_name='Опыт')                   # Опыт работы — 19 лет
    academic_degree = models.CharField(max_length=100, blank=True, verbose_name='Ученая степень')   # Врач высшей категории

    # Редакторы
    content = models.TextField(blank=True, verbose_name='Контент')
    special_note = models.TextField(blank=True, null=True, verbose_name='Примечание')

    class Meta:
        db_table = 'doctors'
        verbose_name = 'Доктор'
        verbose_name_plural = 'Доктора'

    def __str__(self):
        return self.code


class DoctorTiming(models.Model):

    """Расписание приема у определённого доктора."""

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,                               # Приудаление доктора, удалится и его рассписание.
        related_name='dates',
        verbose_name='Доктор'
    )

    organization = models.ForeignKey(
        "organization.Organization",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='doc_timing',
        verbose_name='Организация'
    )
    date = models.DateField(verbose_name='Дата')

    class Meta:
        db_table = 'doctor_dates'
        verbose_name = 'Приём'
        verbose_name_plural = 'Приёмы'

    def __str__(self):
        return f"{self.doctor.full_name} прием {self.date} на {self.organization.name}"


class Timing(models.Model):
    date = models.ForeignKey(
        DoctorTiming,
        on_delete=models.CASCADE,
        related_name='timing',
        verbose_name='Дата приема'
    )
    hour = models.CharField(max_length=5, default=0, verbose_name='Время приема')

    class Meta:
        db_table = 'doctor_times'
        verbose_name = 'Время приема'
        verbose_name_plural = 'Часы приема'

    def __str__(self):
        return str(self.date.date)


class Consultation(models.Model):

    """Консультация у определённого доктора."""

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name='consultation',
        verbose_name='Доктор'
    )

    number = models.CharField(max_length=45, verbose_name='Название')

    question = models.TextField(blank=True, verbose_name='Вопрос')
    answer = models.TextField(blank=True, verbose_name='Ответ')
    status = models.BooleanField(default=False, verbose_name='Статус')
    email = models.EmailField(verbose_name='email')
    date_quest = models.DateTimeField(auto_now_add=True, verbose_name='Дата вопроса')
    date_answer = models.DateTimeField(auto_now=True, verbose_name='Дата ответа')

    class Meta:
        db_table = 'consultation'
        verbose_name = 'Консультация'
        verbose_name_plural = 'Консультации'

    def save(self, *args, **kwargs):
        self.status = True if self.answer else False
        super().save(*args, **kwargs)


class Review(BaseModel):
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name='review',
        verbose_name='Доктор'
    )

    author = models.CharField(max_length=255, verbose_name='Автор')
    review = models.TextField(verbose_name='Отзыв')

    class Meta:
        db_table = 'reviews'
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Video(BaseModel):
    doctor = models.ManyToManyField(
        Doctor,
        related_name='videos',
        verbose_name='Доктор(а)'
    )
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    video = models.TextField(verbose_name='Видео')

    class Meta:
        db_table = 'video'
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'

    def __str__(self):
        return self.title
