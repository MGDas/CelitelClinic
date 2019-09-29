from django.db import models


class ServiceGroup(models.Model):
    code = models.CharField(max_length=15)
    name = models.CharField(max_length=255, verbose_name='Название')

    class Meta:
        db_table = 'service_groups'
        verbose_name = 'Группа услуг'
        verbose_name_plural = 'Группы услуг'


class Service(models.Model):
    code = models.CharField(max_length=15)

    service_group = models.ForeignKey(ServiceGroup,
        on_delete=models.CASCADE,
        related_name='service',
        verbose_name='Группа'
    )

    name = models.CharField(max_length=255, verbose_name='Название')
    time = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'services'
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class PriceType(models.Model):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255, verbose_name='Тип цены')

    class Meta:
        db_table = 'price_types'
        verbose_name = 'Тип цены'
        verbose_name_plural = 'Типы цен'


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

    price = models.DecimalField(max_digits=33, decimal_places=15, verbose_name='Цена')

    class Meta:
        db_table = 'prices'
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'
