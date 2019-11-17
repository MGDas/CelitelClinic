from django.db import models
from clinic.models import BaseModel


class ServiceGroup(BaseModel):
    code = models.CharField(max_length=15)
    name = models.CharField(max_length=255, blank=True, verbose_name='Название')

    class Meta:
        db_table = 'service_groups'
        verbose_name = 'Группа услуг'
        verbose_name_plural = 'Группы услуг'

    def __str__(self):
        return self.name


class Service(models.Model):
    code = models.CharField(max_length=15)

    service_group = models.ForeignKey(ServiceGroup,
        on_delete=models.CASCADE,
        related_name='service',
        verbose_name='Группа'
    )

    name = models.CharField(max_length=255, verbose_name='Название')
    time = models.SmallIntegerField(blank=True, null=True)
    doctors = models.ManyToManyField(
        'doctor.Doctor',
        related_name='services',
        verbose_name='Доктор(а)'
    )

    class Meta:
        db_table = 'services'
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.name


class PriceType(models.Model):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255, verbose_name='Тип цены')

    class Meta:
        db_table = 'price_types'
        verbose_name = 'Тип цены'
        verbose_name_plural = 'Типы цен'

    def __str__(self):
        return self.name


class Price(models.Model):
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name='price',
        verbose_name='Услуга'
    )

    price_type = models.ForeignKey(
        PriceType,
        on_delete=models.CASCADE,
        related_name='price',
        verbose_name='Тип цены'
    )

    price = models.DecimalField(max_digits=33, decimal_places=2, verbose_name='Цена')

    class Meta:
        db_table = 'prices'
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'

    def __str__(self):
        return self.service.name
