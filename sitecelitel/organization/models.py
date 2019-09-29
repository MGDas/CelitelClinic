from django.db import models

def create_name():
    pass

class Organization(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    namefull = models.CharField(max_length=255, verbose_name='Полное название')

    phone_registry = models.CharField(max_length=45, blank=True, verbose_name='Телефон регистрации')
    phone_callcenter = models.CharField(max_length=45, blank=True, verbose_name='Телефон колл-цента')
    address = models.CharField(max_length=255, verbose_name='Адрес')
    operating_mode = models.CharField(max_length=255, verbose_name='График работы')
    site = models.URLField(max_length=45, blank=True, verbose_name='Сайт')
    instagram = models.URLField(max_length=45, blank=True, verbose_name='Инстаграм')
    image = models.ImageField(upload_to=create_name, blank=True, verbose_name='Изображение')

    # Редакторы
    panorama = models.TextField(blank=True, verbose_name='Панорама')
    map = models.TextField(blank=True, verbose_name='Карта')

    class Meta:
        db_table = 'organizations'
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'


class Department(models.Model):
    codeparent = models.CharField(max_length=9, blank=True)
    code = models.CharField(max_length=9, blank=True)

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name='department',
        verbose_name='Организация'
    )

    name = models.CharField(max_length=255, verbose_name='Название')

    class Meta:
        db_table = 'departments'
        verbose_name = 'Депортамент'
        verbose_name_plural = 'Депортаменты'


class Agreement(models.Model):
    code = models.CharField(max_length=36)

    price_type = models.ForeignKey(
        'service.PriceType',
        on_delete=models.CASCADE,
        related_name='agreement',
        verbose_name='Тип цены'
    )

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name='agreement',
        verbose_name='Организация'
    )

    name = models.CharField(max_length=255, verbose_name='Название')

    class Meta:
        db_table = 'agreements'
        verbose_name = 'Соглашение'
        verbose_name_plural = 'Соглашения'
