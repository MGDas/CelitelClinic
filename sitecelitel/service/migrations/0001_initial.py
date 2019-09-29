# Generated by Django 2.2.5 on 2019-09-28 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PriceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255, verbose_name='Тип цены')),
            ],
            options={
                'verbose_name': 'Тип цены',
                'verbose_name_plural': 'Типы цен',
                'db_table': 'price_types',
            },
        ),
        migrations.CreateModel(
            name='ServiceGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=15)),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Группа услуг',
                'verbose_name_plural': 'Группы услуг',
                'db_table': 'service_groups',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=15)),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('time', models.SmallIntegerField(blank=True, null=True)),
                ('service_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service', to='service.ServiceGroup', verbose_name='Группа')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
                'db_table': 'services',
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=15, max_digits=33, verbose_name='Цена')),
                ('price_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='price', to='service.PriceType', verbose_name='Тип цены')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='price', to='service.Service', verbose_name='Услуга')),
            ],
            options={
                'verbose_name': 'Цена',
                'verbose_name_plural': 'Цены',
                'db_table': 'prices',
            },
        ),
    ]