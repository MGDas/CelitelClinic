# Generated by Django 2.2.5 on 2020-01-07 13:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import sitecelitel.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('service', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public', models.BooleanField(default=True, verbose_name='Публикация')),
                ('created', models.DateField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('updated', models.DateField(default=django.utils.timezone.now, verbose_name='Дата обновления')),
                ('code', models.CharField(max_length=36)),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('namefull', models.CharField(blank=True, max_length=255, verbose_name='Полное название')),
                ('phone_registry', models.CharField(blank=True, max_length=45, verbose_name='Телефон регистрации')),
                ('phone_callcenter', models.CharField(blank=True, max_length=45, verbose_name='Телефон колл-цента')),
                ('city', models.CharField(blank=True, max_length=100, verbose_name='Город')),
                ('address', models.CharField(blank=True, max_length=255, verbose_name='Адрес')),
                ('operating_mode', models.TextField(blank=True, verbose_name='График работы')),
                ('site', models.URLField(blank=True, max_length=45, verbose_name='Сайт')),
                ('instagram', models.URLField(blank=True, max_length=45, verbose_name='Инстаграм URL')),
                ('instagram_tag', models.CharField(blank=True, max_length=50, verbose_name='Инстаграм тег')),
                ('image', models.ImageField(blank=True, upload_to=sitecelitel.utils.get_photo, verbose_name='Изображение')),
                ('panorama', models.TextField(blank=True, verbose_name='Панорама')),
                ('map', models.TextField(blank=True, verbose_name='Карта')),
            ],
            options={
                'verbose_name': 'Организация',
                'verbose_name_plural': 'Организации',
                'db_table': 'organizations',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public', models.BooleanField(default=True, verbose_name='Публикация')),
                ('created', models.DateField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('updated', models.DateField(default=django.utils.timezone.now, verbose_name='Дата обновления')),
                ('codeparent', models.CharField(blank=True, max_length=9)),
                ('code', models.CharField(blank=True, max_length=9)),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('organization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='department', to='organization.Organization', verbose_name='Организация')),
            ],
            options={
                'verbose_name': 'Депортамент',
                'verbose_name_plural': 'Депортаменты',
                'db_table': 'departments',
            },
        ),
        migrations.CreateModel(
            name='Agreement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public', models.BooleanField(default=True, verbose_name='Публикация')),
                ('created', models.DateField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('updated', models.DateField(default=django.utils.timezone.now, verbose_name='Дата обновления')),
                ('code', models.CharField(max_length=36)),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('organization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='agreement', to='organization.Organization', verbose_name='Организация')),
                ('price_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='agreement', to='service.PriceType', verbose_name='Тип цены')),
            ],
            options={
                'verbose_name': 'Соглашение',
                'verbose_name_plural': 'Соглашения',
                'db_table': 'agreements',
            },
        ),
    ]
