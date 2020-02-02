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

    non = 'н'
    wom = 'ж'
    man = 'м'

    GENDER = [
        (man, 'Мужчина'),
        (wom, 'Женщина'),
        (non, 'Нет пола')
    ]

    code = models.CharField(max_length=11)                                      # For 1c. Doctor's code
    main_code = models.CharField(max_length=11, blank=True)

    specialization = models.ManyToManyField(
        Specialization,
        blank=True,
        related_name='doctor',
        verbose_name='Специализация'
    )

    department = models.ManyToManyField(
        'organization.Department',
        blank=True,
        related_name='department',
        verbose_name='Депортамент'
    )

    full_name = models.CharField(max_length=255, blank=True, verbose_name='Полное имя')
    gender = models.CharField(max_length=1, choices=GENDER, default=non, blank=True, verbose_name='Пол')
    childish = models.BooleanField(default=False, verbose_name='Детский доктор')
    adult = models.BooleanField(default=False, verbose_name='Взрослый доктор')
    photo = models.ImageField(upload_to=get_photo, blank=True, verbose_name='Фото')
    avatar = models.ImageField(upload_to=get_photo, blank=True, verbose_name='Аватарка')
    experience = models.CharField(max_length=45, blank=True, verbose_name='Опыт')
    academic_degree = models.CharField(max_length=100, blank=True, verbose_name='Ученая степень')

    # Редакторы
    content = models.TextField(blank=True, verbose_name='Контент')
    special_note = models.TextField(blank=True, null=True, verbose_name='Примечание')

    the_best = models.BooleanField(default=False, blank=True, verbose_name="Доктор дня")

    tags = models.ManyToManyField(
        "tag.DoctorTag",
        blank=True,
        related_name='doctors',
        verbose_name='Теги'
    )

    class Meta:
        db_table = 'doctors'
        verbose_name = 'Доктор'
        verbose_name_plural = 'Доктора'
        ordering = ['full_name']

    def __str__(self):
        return self.full_name


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
        return f"{self.date}"


class Timing(models.Model):
    date = models.ForeignKey(
        DoctorTiming,
        on_delete=models.CASCADE,
        related_name='timing',
        verbose_name='Дата приема'
    )
    start = models.CharField(max_length=5, blank=True, verbose_name='Начало')
    end = models.CharField(max_length=5, blank=True, verbose_name='Конец')
    free = models.BooleanField(default=0, verbose_name='Статус')

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

    def __str__(self):
        return self.question

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

    def __str__(self):
        return self.review

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
